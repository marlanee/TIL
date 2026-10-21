# [최대값 구하기]
- 테스트 케이스의 개수 만큼 10개의 수가 주어짐. 그 중 가장 큰 수를 출력해야함
### 풀이 과정
- 입력
  - 테스트 케이스 T
  - 10개의 수

- 풀이 구조
  - for 문으로 반복

- 출력
  - 각 줄의 최대값

### 문제 풀이
```python
def find_max(t, arr):
    arr.sort()
    return arr[9]

T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    print(f"#{t} {find_max(t, numbers)}")
```

### 보완할 점
- 하드코딩 인덱스: `arr[9]` 배열 크기가 변할 경우 안 통함. `arr[-1]`을 사용할 것.
- 불필요한 매개변수: `find_max(t, arr)`에서 함수 내에서 t는 미사용됨. `find_max(arr) 형태로 단순화 필요
- 불필요한 정렬: 큰 수 하나만 찾는데 리스트 전체를 정렬함. `max(arr)` 사용할 것

### 개선안
```python
# 1. 불필요한 매개변수를 제거하고, 내장 max() 함수를 활용해 성능과 안전성을 모두 챙김
def find_max(arr):
    return max(arr)

T = int(input())
for t in range(1, T + 1):
    numbers = list(map(int, input().split()))
    # 2. 함수 호출 시 불필요한 t 인자 전달 제거
    print(f"#{t} {find_max(numbers)}")
```

### 느낀 점
- 함수를 써서 푼 첫 문제다. 잘했다 나 자신.
- 불필요한 매개변수가 있는 것은 아닌지 확인 필요
- 더 빠르고 간편한 함수가 존재한다. 체득화 필요