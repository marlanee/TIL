# TIL · Today I Learned

SSAFY에서 배운 개념과 Python 문제 풀이를 기록합니다. 처음 세운 접근, 틀린 이유, 수정 과정과 코드를 보지 않고 다시 풀어본 결과를 함께 남깁니다.

> PASS는 한 번의 결과. 다시 설명하고 구현할 수 있어야 내 실력.

## 기록 찾아보기

- [학습 노트](./Studies/) — 날짜별 개념 정리와 복습 질문
- [SWEA](./Troubleshooting/SWEA/) — [자료구조](./Troubleshooting/SWEA/Algorithm/)와 난이도별 풀이 [D1·D2](./Troubleshooting/SWEA/D1_D2/) · [D3](./Troubleshooting/SWEA/D3/) · [D4](./Troubleshooting/SWEA/D4/)
- [백준](./Troubleshooting/BOJ/) · [프로그래머스](./Troubleshooting/programmers/) — 플랫폼별 문제 풀이

## 학습 노트

### 최근 학습 · 2026.11

- **알고리즘** — [경주로 건설](./Troubleshooting/programmers/Lv_3/11_09_%EA%B2%BD%EC%A3%BC%EB%A1%9C_%EA%B1%B4%EC%84%A4.py)에서 DFS 시도 후, 같은 칸도 진입 방향에 따라 이후 비용이 달라지는 점을 다익스트라의 상태에 반영했습니다.
- **빅데이터분석기사 실기** — Pandas로 결측치 처리, 3사분위수 이상 거래 필터링, 지점별 집계를 실습했습니다. scikit-learn으로 입력과 타깃을 분리하고 랜덤 포레스트의 분류 정확도를 확인했습니다.

### 월별 기록

[2026.10](./Studies/26.10/) · [2026.09](./Studies/26.09/) · [2026.08](./Studies/26.08/) · [2026.07](./Studies/26.07/)

- [BFS·상태 탐색 질의응답](./Studies/26.09/2026-09-30.md)
- [MST·서로소 집합·요리사 복습](./Studies/26.09/2026-09-29.md)
- [AI 개념 정리](./Studies/26.08/AI_2.md) · [Scene & Source 검색 비교 실험](https://github.com/marlanee/AI_project_2/blob/main/docs/validation.md)

## 대표 알고리즘 풀이

| 대표 풀이 | 복습 포인트 |
| --- | --- |
| [물놀이를 가자 · 10966](./Troubleshooting/SWEA/D4/10966.py) | 다중 시작점 BFS와 최단 거리 |
| [혁진이의 프로그램 검증 · 1824](./Troubleshooting/SWEA/D4/1824.py) | 위치·방향·메모리를 포함한 방문 상태 |
| [요리사 · 4012](./Troubleshooting/SWEA/D4/4012.py) | 재료 조합과 A/B 대칭 |
| [벌꿀채취 · 2115](./Troubleshooting/SWEA/D4/2115.py) | 선택·미선택 분기와 구간별 최대 수익 |
| [보호 필름 · 2112](./Troubleshooting/SWEA/D4/2112.py) | 세 분기, 원상복구, 가지치기와 통과 검사 |
| [최소 스패닝 트리 · 3124](./Troubleshooting/SWEA/D4/3124.py) | Kruskal의 간선 정렬과 집합 병합 |
| [하나로 · 1251](./Troubleshooting/SWEA/D4/1251.py) | Prim에서 현재 트리와 각 정점 사이의 최소 비용 |
| [원자 소멸 시뮬레이션 · 5648](./Troubleshooting/SWEA/D4/5648.py) | 이동, 동시 충돌, 상태 갱신 |

## 복습 루틴

1. **설계하기** — 목표, 상태, 자료구조, 핵심 로직과 종료 조건을 적습니다.
2. **직접 풀기** — 먼저 구현하고, 막힌 지점을 표시합니다.
3. **실패 분석하기** — 접근, 구현, 경계 조건, 효율성 중 어디서 틀렸는지 확인합니다.
4. **말로 설명하기** — 어떤 상태를 저장하고 왜 이 순서로 탐색하는지 설명합니다.
5. **백지 복습하기** — 시간을 두고 기존 코드를 덮어둔 채 다시 구현합니다.

<details>
<summary>복습할 때 확인하는 질문</summary>

- 이 상태 변수는 정확히 무엇을 뜻하는가?
- 선택하지 않는 경우까지 모두 탐색했는가?
- 가지치기로 정답을 놓치지 않는 이유는 무엇인가?
- 마지막 선택의 결과까지 검사하는가?
- 재귀 호출 뒤 무엇을 원상복구해야 하는가?
- 시간복잡도와 실제 실행 비용을 설명할 수 있는가?

</details>

## 기록 템플릿

```text
# 문제 번호. 문제 이름
# 1차 시도: 결과 / 소요 시간
# 복습: 결과 / 다음 복습일

목표:
상태:
자료구조:
핵심 로직:
종료 조건:
시간복잡도:

실패 원인:
수정한 이유:
다음 복습에서 확인할 것:
```
