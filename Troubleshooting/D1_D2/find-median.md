## [중간값 찾기]
N 값과 N개의 홀수가 주어짐. 중간값을 출력해야함

### 풀이 과정
```python
T = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
median = numbers[T // 2]
print(median)
```

### 1. 발생한 문제
- 에러 없음
- 변수 설정 아쉬움: T 대신 문제에 주어진 N 사용할 것

### 2. 개선 방법
```python
def find_median(n, arr):
  arr.sort()
  return arr[n // 2]

n = int(input())
numbers = list(map(int, input().split()))
print(fint_median(n, numbers))
```
### 3. 핵심 교훈
- 함수로 문제를 풀어보았다.
- 이 방법을 쓸 경우 n으로 길이를 먼저 파악해서, 연산 시간이 줄어든다고 한다.
- 그리고 뭔가 있어 보인다.