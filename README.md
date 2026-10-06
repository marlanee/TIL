<div align="center">

<h1>📚 TIL · Today I Learned</h1>

<p><strong>오늘 배운 것을 내 말로 정리하고, 백지 복습으로 내 것으로 만드는 기록.</strong></p>

<p>
  <img src="https://img.shields.io/badge/SSAFY-Learning-2563EB?style=flat-square" alt="SSAFY" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Algorithm-Problem%20Solving-16A34A?style=flat-square" alt="Algorithm" />
  <img src="https://img.shields.io/badge/Review-From%20Scratch-F59E0B?style=flat-square" alt="백지 복습" />
</p>

</div>

---

## 👋 About This Repository

SSAFY에서 배우는 개념과 Python 알고리즘 풀이를 기록합니다.

정답 코드뿐 아니라 처음 세운 접근, 틀린 이유, 수정 과정,
복습하며 다시 이해한 내용을 함께 남깁니다.

> **PASS는 한 번의 결과. 다시 설명하고 구현할 수 있어야 내 실력.**

## 🗂️ Repository Guide

| 경로 | 내용 |
| :--- | :--- |
| [Studies](./Studies/) | 날짜별 학습 노트와 개념 복습 |
| [Troubleshooting/Algorithm](./Troubleshooting/Algorithm/) | 기본 알고리즘·자료구조 연습 |
| [Troubleshooting/D1_D2](./Troubleshooting/D1_D2/) | 기초 문법과 구현 문제 |
| [Troubleshooting/D3](./Troubleshooting/D3/) | 구현·탐색 등 문제 풀이 |
| [Troubleshooting/D4](./Troubleshooting/D4/) | 심화 알고리즘과 모의 SW 역량테스트 풀이 |

## 📝 Learning Notes

| 월 | 학습 기록 |
| :---: | :--- |
| **2026.07** | [7월 학습 노트](./Studies/26.07/) |
| **2026.08** | [8월 학습 노트](./Studies/26.08/) |
| **2026.09** | [9월 학습 노트](./Studies/26.09/) |

### 바로 읽기

- [AI 개념 정리](./Studies/26.08/AI_2.md)
- [MST·서로소 집합·요리사 복습](./Studies/26.09/2026-09-29.md)
- [BFS·상태 탐색 핵심 질의응답](./Studies/26.09/2026-09-30.md)

## 🧩 Algorithm Archive

문제 번호를 모으는 것만큼,
**어떤 상태를 저장하고 어떤 경우를 탐색해야 하는지**를 이해하는 데 집중합니다.

| 주제 | 대표 풀이 | 학습 포인트 |
| :--- | :--- | :--- |
| **BFS** | [10966 · 물놀이를 가자](./Troubleshooting/D4/10_07_10966.py) | 다중 시작점과 최단 거리 |
| **상태 탐색** | [1824 · 혁진이의 프로그램 검증](./Troubleshooting/D4/10_02_1824.py) | 위치·방향·메모리를 포함한 방문 상태 |
| **조합 탐색** | [4012 · 요리사](./Troubleshooting/D4/10_05_4012.py) | 재료 조합과 A/B 대칭 |
| **부분집합 탐색** | [2115 · 벌꿀채취](./Troubleshooting/D4/10_08_2115.py) | 선택·미선택 분기와 구간별 최대 수익 |
| **백트래킹** | [2112 · 보호 필름](./Troubleshooting/D4/10_08_2112.py) | 세 분기, 원상복구, 가지치기와 통과 검사 |
| **Kruskal** | [3124 · 최소 스패닝 트리](./Troubleshooting/D4/10_06_3124.py) | 간선 정렬과 대표자끼리의 집합 병합 |
| **Prim** | [1251 · 하나로](./Troubleshooting/D4/1251.py) | 현재 MST와 각 정점 사이의 최소 비용 |
| **시뮬레이션** | [5648 · 원자 소멸 시뮬레이션](./Troubleshooting/D4/5648.py) | 이동, 동시 충돌과 상태 갱신 |

## 🔁 Study Routine

1. **설계하기**  
   목표, 상태, 자료구조, 핵심 로직과 종료 조건부터 적습니다.

2. **직접 풀기**  
   먼저 구현하고, 막힌 지점을 구체적으로 확인합니다.

3. **실패 분석하기**  
   접근의 문제인지, 구현·경계 조건·효율성의 문제인지 구분합니다.

4. **말로 설명하기**  
   핵심 로직이 왜 맞는지 질의응답으로 확인합니다.

5. **백지 복습하기**  
   일정 기간 뒤 기존 코드 없이 다시 구현합니다.

### 복습할 때 확인하는 질문

- 이 상태 변수는 정확히 무엇을 뜻하는가?
- 선택하지 않는 경우까지 모두 탐색했는가?
- 가지치기로 정답을 놓치지 않는 이유는 무엇인가?
- 마지막 선택의 결과까지 검사하는가?
- 재귀 호출 뒤 무엇을 원상복구해야 하는가?
- 시간복잡도와 실제 실행 비용을 설명할 수 있는가?

## ✍️ 기록 템플릿

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

---

<div align="center">

<p><strong>오늘 이해한 것을, 다음에는 혼자 구현할 수 있도록.</strong></p>

<p>작은 기록을 쌓아가는 중입니다. 🌱</p>

</div>
