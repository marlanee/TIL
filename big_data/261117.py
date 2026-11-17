# import pandas as pd
# from io import StringIO

# csv_text = """id,branch,age,amount
# 1,Seoul,25,120000
# 2,Seoul,32,180000
# 3,Busan,28,90000
# 4,Busan,35,
# 5,Seoul,42,210000
# 6,Daegu,23,80000
# 7,Daegu,31,150000
# 8,Busan,45,230000
# 9,Daegu,38,
# 10,Seoul,29,110000
# """

# df = pd.read_csv(StringIO(csv_text))

# # 1. amount의 결측치를 전체 amount의 중앙값으로 대체하시오
# df['amount'] = df['amount'].fillna(df['amount'].median())
# # 2. 나이가 30세 이상인 고객만 추출하시오
# target = df[df['age'] >= 30]
# # 3. 지점별 amount의 평균을 계산하시오
# branch_mean = df.groupby('branch')['amount'].mean()
# # 4. 평균이 가장 높은 지점의 이름과 해당 평균값을 출력하시오
# print(branch_mean.idxmax(), branch_mean.max())
# # 5. 평균값은 소수점 이하를 버리고 정수로 출력하시오
# print(f'{branch_mean.idxmax()}, {round(branch_mean.max())}')
# # int()가 소수점 버림. round()가 소수점 반올림. :.2f 는 반올림이랬지?

# import pandas as pd
# from io import StringIO # gpt야, io랑 StringIO는 무슨 기능의 라이브러리야? 라이브러리를 가져온다

# csv_text = """id,branch,sales
# 1,Seoul,100
# 2,Busan,120
# 3,Seoul,150
# 4,Daegu,130
# 5,Busan,140
# 6,Daegu,160
# 7,Seoul,170
# 8,Busan,180
# 9,Daegu,190
# 10,Seoul,1500
# """

# df = pd.read_csv(StringIO(csv_text))    # StringIO = 문자열을 텍스트 파일처럼 사용할 수 있도록 만드는 클래스

# # 1. sales의 25% 분위수(Q1), 75%의 분위수(Q3)를 구하시오
# Q1 = df['sales'].quantile(0.25)
# Q3 = df['sales'].quantile(0.75)
# # 2. IQR(Q3 - Q1)을 계산하시오
# IQR = Q3 - Q1
# # 3. Q1 - 1.5 x IQR 미만이거나 Q3 + 1.5 x IQR 초과인 데이터를 이상치로 판단하여 제거하시오.
# # 이거는 무슨 기준이야? 실제로 문제에도 이렇게 나오나? 이게 이상치를 판단하는 기본적인 방법이야?
# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR
# normal = df[(df['sales'] >= lower) & (df['sales'] <= upper)]
# # 4. 이상치 제거 후 지점별 sales의 합계를 계산하시오.
# branch_sum = df.groupby('branch')['sales'].sum()
# # 5. 합계가 두 번째로 높은 지점의 매출 합계를 출력하시오
# branch_sum = branch_sum.sort_values(ascending=False)
# print(branch_sum.iloc[1])


# 2단계. 작업형 2 실전 구현
# 1. 필요한 라이브러리와 함수를 직접 import 하시오.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import roc_auc_score
# 2. train.csv, test.csv를 읽으시오
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
# 3. 독립변수와 종속변수를 분리하고 고객 번호를 학습 대상에서 제외하시오
X = train.drop(columns=['customer_id', 'default'])
y = train['default']
X_test = test.drop(columns=['customer_id'])
# 4. 학습용 데이터를 훈련 80%, 검증 20%
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
# 5. 수치형 변수의 결측치는 훈련 데이터의 중앙값으로 처리하시오.
# 수치형 변수의 결측치가 어느 열에 있는지 어떻게 찾지? 일단 X_train을 출력하면 debt만 결측치가 있는 것 같긴 한데..
# 만약 결측치를 가진 열이 여러개라면? 흠.. 그냥 다 채우자.
medians = X_train.median(numeric_only=True)

X_train = X_train.fillna(medians)
X_val = X_val.fillna(medians)
test = test.fillna(medians)

# 6. job을 원핫 인코딩하고 훈련,검증,테스트 데이터의 열을 일치시키시오  # 구글 검색 찬스 사용했음
X_train = pd.get_dummies(X_train, columns=['job'], dtype=int)   # pd.get_dummies = 원핫 인코딩
X_val = pd.get_dummies(X_val, columns=['job'], dtype=int)
X_test = pd.get_dummies(X_test, dtype=int)
# 질문. 그냥 원핫 인코딩하라는 요구사항인데, dtype=int를 굳이 해야되나? # 이것 또한 구글 검색 찬스 사용
X_val = X_val.reindex(columns=X_train.columns, fill_value=0)
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)
# 정답 데이터 - y에는 열 일치 시키지 말라던데 사실이야?
# 7. 랜덤 포레스트 분류 모델을 학습하시오
model = RandomForestClassifier(random_state=42) # random_state=42는 고정인가? 아무렇게나 해도 되나?
model.fit(X_train, y_train)
# 8. 검증 데이터의 ROC-AUC를 출력하시오
val_proba = model.predict_proba(X_val)[:, 1]
score = roc_auc_score(y_val, val_proba)    # 하 이게 아니었던가? pred가 아닌가? proba인가?
print(score)
# 9. 테스트 데이터의 연체 확률을 예측하시오
test_proba = model.predict_proba(X_test)[:, 1]
# 10. 다음 형식으로 result.csv.를 생성하시오. 별도의 인덱스 열을 저장하지 마시오
result = pd.DataFrame({
    'customer_id': test['customer_id'],
    'default': test_proba
})

result.to_csv('result.csv', index=False)

print(result.head())
print(result.shape)