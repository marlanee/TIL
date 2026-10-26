import sys
import user_solution as user

CMD_INIT = 1
CMD_HIRE = 2
CMD_FIRE = 3
CMD_UPDATE_SOLDIER = 4
CMD_UPDATE_TEAM = 5
CMD_BEST_SOLDIER = 6


def run(data):
    numQuery = next(data)
    isCorrect = False

    for _ in range(numQuery):
        cmd = next(data)

        if cmd == CMD_INIT:
            user.init()
            isCorrect = True

        elif cmd == CMD_HIRE:
            mID = next(data)
            mTeam = next(data)
            mScore = next(data)
            user.hire(mID, mTeam, mScore)

        elif cmd == CMD_FIRE:
            mID = next(data)
            user.fire(mID)

        elif cmd == CMD_UPDATE_SOLDIER:
            mID = next(data)
            mScore = next(data)
            user.updateSoldier(mID, mScore)

        elif cmd == CMD_UPDATE_TEAM:
            mTeam = next(data)
            mChangeScore = next(data)
            user.updateTeam(mTeam, mChangeScore)

        elif cmd == CMD_BEST_SOLDIER:
            mTeam = next(data)
            userAns = user.bestSoldier(mTeam)
            ans = next(data)

            if userAns != ans:
                isCorrect = False

        else:
            isCorrect = False

    return isCorrect


def main(stream):
    # 줄바꿈과 관계없이 정수를 순서대로 읽는다.
    data = (
        int(token)
        for line in stream
        for token in line.split()
    )

    T = next(data)
    MARK = next(data)

    for tc in range(1, T + 1):
        score = MARK if run(data) else 0
        print(f"#{tc} {score}")


if __name__ == "__main__":
    # 실행할 때 입력 파일명을 지정할 수 있다.
    if len(sys.argv) > 1:
        with open(sys.argv[1], "rb") as input_file:
            main(input_file)
    else:
        main(sys.stdin.buffer)