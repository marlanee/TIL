
import pandas as pd
from io import StringIO

csv_text = """customer_id,branch,age,amount
1,Gangnam,23,120000
2,Hongdae,31,85000
3,Gangnam,45,
4,Busan,29,210000
5,Hongdae,,95000
6,Busan,38,180000
7,Gangnam,27,155000
8,Hongdae,35,125000
9,Busan,41,
10,Gangnam,33,90000
"""

df = pd.read_csv(StringIO(csv_text))



# 컬럼이 하나인 dataframe이 series인가? 답해줘

# amount가 결측치인 행 제거하기
new_df = df.dropna(subset=['amount'])    # subset은 뭐야?    얘는 fillna랑 다르게 amount가 맨 뒤에 붙네.
# 75% 분위수 Q3 계산
target_amount = new_df['amount'].quantile(0.75) # quantile이 뭐야? 하위 75%?
# Q3 이상인 고객만 추출
target = new_df[new_df['amount'] >= target_amount]
# branch별로 그룹화, 고객 수 계산
branch_count = target.groupby('branch').size()  # size는 행 개수를 구하는 메서드다.
# 고객 수가 가장 많은  지점의 이름과 고객 수 출력
print(branch_count.idxmax(), branch_count.max())    # idxmax() = 가장 큰 값의 인덱스 이름 , max() 가장 큰 값