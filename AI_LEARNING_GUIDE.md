# VS Code 알고리즘 학습 AI 사용 안내

설정·검증 날짜: 2026-11-03 (한국 시간)
적용 프로젝트: `C:\Users\SSAFY\Desktop\TIL`

## 설정된 항목

| 항목 | 결과 |
| --- | --- |
| VS Code 1.144.1 | 한국어 언어 팩 설치, 표시 언어 `ko` 적용 및 재시작 완료. 파일·편집·보기 메뉴에서 한국어 확인 |
| 공식 OpenAI Codex (`openai.chatgpt`) | 기존 설치 26.1021.22027 유지, ChatGPT 계정 인증 및 실제 응답 확인 |
| 공식 Anthropic Claude Code (`anthropic.claude-code`) | 기존 설치 2.1.317 유지, 기존 Claude Pro 인증 및 실제 응답 확인 |
| Ruff (`charliermarsh.ruff`) | 2026.92.0 새로 설치. Python 정적 오류·품질 검사 활성화 |
| 한국어 언어 팩 (`ms-ceintl.vscode-language-pack-ko`) | 1.131.2026090407 새로 설치 |

ChatGPT 로그인은 확인했지만 Plus 등 정확한 요금제 이름은 별도로 확인하지 않았다.
추가 API 키를 생성하거나 입력하지 않았다. 현재 계정은 이미 인증되어 있어 추가 로그인 입력이 필요하지 않았다.

## 매일 사용하는 방법

1. 이 TIL 폴더를 프로젝트 루트로 열고 Python 풀이 파일을 연다.
2. `Ctrl+S`로 저장한다. Python/Pylance와 Ruff가 문법·정의되지 않은 이름·일부 실수 가능성을 문제 패널에 표시한다. `Ctrl+Shift+M`으로 확인한다. 검사 결과에 따라 자동으로 코드를 고치거나 서식을 바꾸지 않는다.
3. 논리·복잡도·학습 힌트가 필요하면 명령 팔레트(`Ctrl+Shift+P`)에서 `작업 실행`을 선택한다.
4. `AI 힌트 리뷰: Codex (현재 파일)` 또는 `AI 힌트 리뷰: Claude (현재 파일)`을 실행한다. 결과는 작업 터미널에 표시된다. 실행 전 반드시 검토할 Python 파일을 현재 편집기로 선택하고 저장한다. 설정 파일이나 이 안내 파일을 선택하면 그 파일이 리뷰 대상이 된다.
5. 이어지는 대화는 Codex 또는 Claude Code 확장 패널에서 현재 파일을 첨부하고 요청한다. 새 대화를 시작하면 새 프로젝트 지침을 읽는다. 이미 열려 있던 대화에는 지침을 다시 읽도록 요청한다.

두 수동 리뷰 작업은 각각 확장에 포함된 공식 실행 파일을 사용한다. 별도 CLI 설치는 필요하지 않다. 작업을 실행할 때 해당 서비스로 검토할 코드와 지침이 전달되고 계정의 사용량을 소비한다. 저장만으로 AI를 호출하지 않는다.

## 학습 지침

`AGENTS.md`를 Codex가 읽고, `CLAUDE.md`가 같은 지침을 불러온다.

- 기본 답변은 한국어다.
- 정답·전체 풀이·완성 코드를 명시적으로 요청하기 전에는 정답을 공개하지 않는다.
- 사용자의 접근을 먼저 이해하고, 논리 오류·시간/공간 복잡도·코드 품질을 평가한다.
- 처음에는 중요한 문제 최대 3개와 다음 힌트 하나를 제공한다.
- 문제 설명이 없거나 실행하지 않았으면 판단의 한계를 밝힌다.
- 기본 리뷰는 읽기만 한다. 사용자 풀이와 입력 파일을 자동 수정·실행하지 않는다.

이는 모델이 따르는 프로젝트 지침이며, 모든 상황에서 정답 공개를 기술적으로 차단하는 장치는 아니다.

## 저장 시 자동화의 범위

설치된 두 공식 AI 확장의 공개 설정과 명령에는 `저장할 때마다 AI 리뷰` 기능이 없다. Claude의 `autosave`는 Claude가 파일을 읽고 쓰기 전에 저장하는 기능으로, 저장 시 AI 리뷰와 다르다.

따라서 지원되는 범위는 다음과 같이 구성했다.

- 파일 열기·편집·저장: 로컬 정적 검사. AI 서비스 호출 없음.
- 사용자 작업 실행: AI가 논리, 복잡도, 코드 품질을 힌트 방식으로 리뷰.

완전한 AI 저장 자동화를 하려면 별도 저장 감지 확장/도구가 필요하다. 이번에는 설치하지 않았다. 정적 검사는 알고리즘의 정답 여부나 시간 초과를 보장하지 않는다.

## 검증한 내용

- 두 공식 확장의 설치 상태와 기존 계정 인증 확인.
- 두 작업의 실제 명령을 별도의 짧은 평균 함수 예제로 실행, 모두 종료 코드 0 확인.
- 두 AI가 빈 입력의 문제, O(N) 시간/O(1) 공간, 한국어 힌트를 반환했고 정답 코드를 공개하지 않았음을 확인.
- Ruff 실행 파일이 정의되지 않은 변수(F821)를 감지함을 확인.
- VS Code에서 별도 Python 예제를 저장한 뒤 문제 패널에 Ruff의 가변 기본 인자 경고(B006)가 표시됨을 확인.
- 한국어 메뉴 표시 확인.
- 테스트에 사용한 임시 파일 삭제. 실제 풀이와 입력 파일은 실행하거나 수정하지 않음.
- 변경 전부터 존재했던 모든 프로젝트 파일의 해시를 비교하여 변경 0개 확인.

## 변경 파일과 보존

새 프로젝트 파일:

- `AGENTS.md`: 두 AI가 공유하는 한국어 학습·리뷰 지침.
- `CLAUDE.md`: 공통 지침 불러오기.
- `.vscode/settings.json`: Ruff 검사와 Python 자동 수정 방지 설정.
- `.vscode/extensions.json`: 공식 AI/Python/검사/한국어 확장 권장 목록.
- `.vscode/tasks.json`: 현재 파일 수동 AI 힌트 리뷰 작업 2개.
- `AI_LEARNING_GUIDE.md`: 이 안내.

기존 사용자 설정에는 `chatgpt.localeOverride: "ko"`만 추가했고, `C:\Users\SSAFY\.vscode\argv.json`에는 `locale: "ko"`만 추가했다. 기존 주석과 다른 설정은 유지했다. 변경 전 원본은 이 작업 폴더의 `work\before-settings`에 보관했다.

기존 Git 변경 `Troubleshooting/solution.py`, `Troubleshooting/sample_input.txt` 및 미추적 풀이 `Troubleshooting/SWEA/D5/11_06_1798.py`는 그대로 두었다. 커밋·푸시는 하지 않았다.

## 수동 조치 및 남는 제한

- 지금 추가 로그인·승인은 필요 없다. 나중에 인증이 만료되면 각 확장의 Sign in을 통해 기존 구독 계정으로 직접 로그인한다.
- 새 AI 대화를 시작하거나 지침 파일을 읽도록 요청한다.
- Claude 등 일부 확장의 자체 버튼, Ruff 등의 진단 문구는 영어로 남을 수 있다. VS Code 한국어 팩의 번역 범위와 별개다.
- 설정은 이 TIL 프로젝트에 적용된다. 다른 폴더에는 학습 지침이 자동 복사되지 않는다.
- 리뷰 작업은 현재 설치된 확장 버전의 실행 파일 경로를 사용한다. 확장 업데이트 후 이전 버전 폴더가 제거되면 `.vscode/tasks.json`의 `command` 경로를 새 버전에 맞춰 갱신해야 한다. 확장 패널의 대화는 계속 사용할 수 있다.

## 공식 참고 문서

- [VS Code 표시 언어](https://code.visualstudio.com/docs/configure/locales)
- [OpenAI Codex IDE 확장](https://learn.chatgpt.com/docs/codex/ide)
- [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Anthropic Claude Code VS Code 확장](https://code.claude.com/docs/en/vs-code)
- [Claude 프로젝트 지침](https://code.claude.com/docs/en/memory)
- [VS Code Python 검사](https://code.visualstudio.com/docs/python/linting)
