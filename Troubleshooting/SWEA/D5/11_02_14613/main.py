a = [i for i in range(10, -1, -1)]

print(a)



"""공개 C++/Java main을 참고한 로컬 채점 드라이버. 풀이 구현 없음.

기본: python main.py                     (직접 만든 seed_input.txt 사용)
      python main.py downloaded_input.txt (공개 드라이버의 시드 입력 형식)
      python main.py --format literal local_input.txt (자체 학습 입력 형식)
      python main.py -                   (표준 입력)

SWEA 원본/공식 Python 지원은 미확인. 출처와 차이점은 README.md 참고.
"""

import argparse
import sys
from pathlib import Path

import solution

CMD_INIT = 100
CMD_MAKE_LIST = 200
CMD_COPY_LIST = 300
CMD_UPDATE_ELEMENT = 400  # 공개 소스의 CMD_UNDATE_ELEMENT와 같은 번호
CMD_ELEMENT = 500
MAX_LENGTH = 200_000


class InputFormatError(ValueError):
    """입력 형식이 맞지 않을 때 발생한다."""


class Tokens:
    def __init__(self, stream):
        self.items = (token for line in stream for token in line.split())

    def text(self):
        try:
            return next(self.items)
        except StopIteration:
            raise InputFormatError("입력이 중간에 끝났습니다.") from None

    def integer(self):
        value = self.text()
        try:
            return int(value)
        except ValueError:
            raise InputFormatError(f"정수가 필요합니다: {value!r}") from None

    def finish(self):
        extra = next(self.items, None)
        if extra is not None:
            raise InputFormatError(f"모든 케이스를 읽은 뒤 남은 입력: {extra!r}")


class Generator:
    """공개 드라이버의 32비트 난수 생성기. 문제 해법과 무관하다."""

    def __init__(self, seed):
        self.state = seed & 0xFFFFFFFF

    def rand(self):
        self.state = (self.state * 214013 + 2531011) & 0xFFFFFFFF
        return (self.state >> 16) & 0x7FFF


def generate_name(seed):
    rng = Generator(seed)
    length = rng.rand() % 20 + 1
    return "".join(chr(rng.rand() % 26 + ord("a")) for _ in range(length))


def generate_list(seed, buffer):
    rng = Generator(seed)
    length = ((rng.rand() << 15) + rng.rand()) % MAX_LENGTH + 1
    for i in range(length):
        buffer[i] = rng.rand()
    return length


def read_name(tokens, input_format):
    if input_format == "seed":
        return generate_name(tokens.integer())
    name = tokens.text()
    if not (1 <= len(name) <= 20 and all("a" <= c <= "z" for c in name)):
        raise InputFormatError("literal 이름은 길이 1~20의 영문 소문자여야 합니다.")
    return name


def grade(stream, api=solution, input_format="seed", diagnostics=None):
    """[(테스트 번호, 점수), ...]를 반환한다. api는 테스트용으로 교체 가능.

    입력 형식만 점검하며 API의 이름 존재 여부/인덱스 범위는 풀이에 맡긴다.
    공개 main과 같이 init은 정답 상태를 True로, 오답 조회는 False로 바꾼다.
    """
    if input_format not in ("seed", "literal"):
        raise InputFormatError("input_format은 seed 또는 literal이어야 합니다.")
    tokens = Tokens(stream)
    test_count, mark = tokens.integer(), tokens.integer()
    if test_count < 1 or mark <= 0:
        raise InputFormatError("T는 1 이상, MARK는 양수여야 합니다.")
    buffer = [0] * MAX_LENGTH  # 공개 main처럼 여러 makeList 호출에서 재사용
    results = []
    for tc in range(1, test_count + 1):
        query_count = tokens.integer()
        if query_count < 0:
            raise InputFormatError("Q는 음수일 수 없습니다.")
        correct = False
        for q in range(1, query_count + 1):
            cmd = tokens.integer()
            if cmd == CMD_INIT:
                api.init()
                correct = True
            elif cmd == CMD_MAKE_LIST:
                name = read_name(tokens, input_format)
                if input_format == "seed":
                    length = generate_list(tokens.integer(), buffer)
                else:
                    length = tokens.integer()
                    if not 1 <= length <= MAX_LENGTH:
                        raise InputFormatError("리스트 길이는 1~200,000이어야 합니다.")
                    for i in range(length):
                        value = tokens.integer()
                        if not 0 <= value <= 32767:
                            raise InputFormatError("원소 값은 0~32,767이어야 합니다.")
                        buffer[i] = value
                api.makeList(name, length, buffer)
            elif cmd == CMD_COPY_LIST:
                dest = read_name(tokens, input_format)
                src = read_name(tokens, input_format)
                api.copyList(dest, src, tokens.integer() != 0)
            elif cmd == CMD_UPDATE_ELEMENT:
                name = read_name(tokens, input_format)
                index, value = tokens.integer(), tokens.integer()
                api.updateElement(name, index, value)
            elif cmd == CMD_ELEMENT:
                name = read_name(tokens, input_format)
                index, expected = tokens.integer(), tokens.integer()
                actual = api.element(name, index)
                if actual != expected:
                    correct = False
                    if diagnostics is not None:
                        print(f"TC {tc}, query {q}: element({name!r}, {index}) "
                              f"expected={expected}, actual={actual!r}", file=diagnostics)
            else:
                # 공개 main의 단순 0점 처리 대신, 잘못된 파싱을 바로 알린다.
                raise InputFormatError(f"TC {tc}, query {q}: 알 수 없는 명령 {cmd}")
        results.append((tc, mark if correct else 0))
    tokens.finish()
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", nargs="?", help="입력 파일 경로. -이면 표준 입력")
    parser.add_argument("--format", choices=("seed", "literal"), default="seed")
    parser.add_argument("--quiet", action="store_true", help="오답 상세 표시 생략")
    args = parser.parse_args()
    input_path = args.input or str(Path(__file__).with_name(
        "seed_input.txt" if args.format == "seed" else "local_input.txt"))
    stream = None
    try:
        stream = sys.stdin if input_path == "-" else open(input_path, encoding="utf-8-sig")
        results = grade(stream, input_format=args.format,
                        diagnostics=None if args.quiet else sys.stderr)
    except NotImplementedError as error:
        print(f"미구현: {error}. solution.py의 TODO를 직접 구현하세요.", file=sys.stderr)
        return 2
    except (OSError, InputFormatError) as error:
        print(f"입력 오류: {error}", file=sys.stderr)
        return 2
    finally:
        if stream is not None and stream is not sys.stdin:
            stream.close()
    for tc, score in results:
        print(f"#{tc} {score}")
    return 0 if all(score > 0 for _, score in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
