# 연월일 달력
- 테스트 개수 T 와 숫자 8자리가 입력됨
- 날짜의 유효성을 판단 후 양식에 맞게 출력해야 함
- 소요 시간: 1시간 30분
---
### 아쉬운 점
- 숫자 8자리를 문자열로 바꿔서 슬라이싱 하면 되는 문제였음
- 그걸 모르고 리스트에 담고 map에 담고 난리를 쳤음
- 문자열 슬라이싱 하는 방법을 익혀야 함
- 숨어 있는 버그를 체크해야 함.
    - 처음에 짠 코드는 0일때 버그가 발생했음
---
### 소감
- 이별 4일차, 많이 힘들다.
- 이런 쉬운 문제에 1시간 30분을 썼다는게 믿기지 않는다
- D1 문제는 30분 제한을 두고 풀자


```python
# 테스트 케이스 개수 T 정의
T = int(input())

month_28 = [2]
month_30 = [4, 6, 9, 11]
month_31 = [1, 3, 5, 7, 8, 10, 12]

for i in range(1, T + 1):
    date = input().strip()

    year_str = date[:4]
    month_str = date[4:6]
    day_str = date[6:]

    month = int(month_str)
    day = int(day_str)

    # 1일 이상인지 체크하는 양쪽 범위 조건 추가
    # elif와 else를 사용하여 불필요한 month_None 리스트 제거
    if month in month_28 and 1 <= day <= 28:
        print(f'#{i} {year_str}/{month_str}/{day_str}')
    elif month in month_30 and 1 <= day <= 30:
        print(f'#{i} {year_str}/{month_str}/{day_str}')
    elif month in month_31 and 1 <= day <= 31:
        print(f'#{i} {year_str}/{month_str}/{day_str}')
    else:
        # 1~12월이 아니거나, 일자 범위를 벗어난 모든 경우 -1
        print(f'#{i} -1')
```