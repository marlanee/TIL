# 261116. 
"""
1. 기존 학습 백지 복습
2. 작업형 제 1유형: 데이터 전처리
3. 작업형 제 2유형: 회귀 모델 및 평가지표
4. 작업형 제 3유형: 가설검정
5. 최종 백지 복습 및 평가
? 작업형이 뭐지? - 빅분기 실기는 작업형3 문제만 존재한다.
Q. 라이브러리 설치부터 from~import까지 직접 해야되는지? 
"""

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     'Name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
#     'Department': ['IT', 'HR', 'IT', 'HR', 'IT', 'Sales', 'Sales', 'IT'],
#     'Salary': [3000, 4000, 5000, 6000, 7000, 8000, 4000, np.nan],
#     'Age': [25, 32, 35, 28, 40, 45, 30, 38]
# })

# 데이터 확인
# print(df)

# 아래부터 문제 풀이

# 문제1. 데이터 전처리와 데이터 누수
# for col in ['Age', 'Salary']:
#     medain = X_train[col].median()
#     X_train = X_train[col].fillna(medain)
#     X_test[col] = X_test[col].fillna(medain)

# 작업형 제1유형 실전 문제 - 부서별 평균 연봉 계산, 평균 연봉이 가장 높은 부서의 이름과 해당 평균 연봉 출력
# groupbu() 문법 기본 구조: df.groupby('그룹화 기준')['계산 대상'].mean()

# new_df = df.groupby('Department')['Salary'].mean()
# print(new_df.idxmax())
# print(new_df.max())

# 작업형 제1유형 - 복합 데이터 처리
# 1. Salary의 결측치를 전체 Salary의 중앙값으로 대체하시오
# df['Salary'] = df['Salary'].fillna(df['Salary'].median())
# 2. 나이가 30세 이상인 직원만 추출하시오
# target = df[df['Age'] >= 30]
# 3. 추출된 직원들의 부서별 평균 연봉을 계산하시오.
# dept_mean = target.groupby('Department')['Salary'].mean()
# 4. 평균 연봉이 가장 높은 부서와 해당 평균 연봉을 출력하시오.
# print(dept_mean.idxmax(), dept_mean.max())

# 작업형 제1유형 - 문제3. 정렬 및 데이터 집계
# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     'ID': range(1, 11),
#     'Score': [85, 92, 77, 65, 98, 55, 87, 73, 91, 80],
#     'Hours': [5, 8, 4, 3, 10, 2, 7, 4, np.nan, 6],
#     'Class': ['A', 'B', 'A', 'B', 'A',
#               'B', 'A', 'B', 'A', 'B']
# })

# 아래부터 문제 풀이

# 1. Hours의 결측치를 전체 Hours의 평균으로 대체하시오
# df['Hours'] = df['Hours'].fillna(df['Hours'].mean())
# 2. Score를 기준으로 내림차순 정렬하시오.
# sort_score_df = df.sort_values(by='Score', ascending=False) # by, ascending
# 3. 성적이 가장 높은 상위 30%의 학생들을 추출하시오
# n = int(len(df) * 0.3)
# target_df = sort_score_df.iloc[:n]
# 4. 추출된 학생들의 Hours의 표본 표준편차를 구하시오
# target_std = target_df['Hours'].std()
# 5. 결과를 소수점 셋째 자리에서 반올림하여 소수점 둘째 자리까지 출력하시오
# print(f'{target_std:.2f}')

# 3단계. 작업형 제2유형 - 회귀 모델
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor


# df = pd.DataFrame({
#     'Area': [30, 45, 50, 60, 70, 85, 90, 100, 110, 120],
#     'Rooms': [1, 2, 2, 3, 3, 3, 4, 4, 5, 5],
#     'Years': [15, 10, 8, 12, 5, 3, 7, 2, 4, 1],
#     'Price': [150, 200, 230, 280, 350,
#               420, 450, 510, 560, 620]
# })

# # 아래부터 문제 풀이
# # 질문. sklearn.model_selection import train_test_split이나, RandomForestRegressor은 외워야하는지?
# # 1. Price를 예측 대상 y로, 나머지 열을 입력 데이터 x로 분리하시오.
# X = df.drop(columns='Price')    # 행이 아니라 열이므로, columns=가 필수적이다.
# y = df['Price']
# # 2. 훈련 데이터 80%, 검증 데이터 20%로 분리하시오. random_state=42를 사용하시오.
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )
# # 3. RandomForestRegressor를 선언하시오.
# model = RandomForestRegressor(n_estimators=100, random_state=42)
# # 4. 모델을 학습하시오.
# model.fit(X_train, y_train)
# # 검증 데이터의 주택 가격을 예측하고 출력하시오
# pred = model.predict(X_test)
# # print(pred)

# # 실습 문제 - 회귀 모델 평가
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# from math import sqrt
# # 1. y_test와 pred를 이용하여 MAE를 계산하시오.
# MAE = mean_absolute_error(y_test, pred)
# # 2. MSE를 계산하시오
# MSE = mean_squared_error(y_test, pred)  # 오차가 왜 이렇게 크지?. 그리고 pred와 y_test의 순서는 바껴도 상관없나?
# # 3. MSE를 이용하여 RMSE를 계산하시오
# RMSE = sqrt(MSE)    # 오? MAE랑 비슷하네. 우연인가?
# # 4. R^2를 계산하시오
# R2 = r2_score(y_test, pred) # 이건 또 1이랑 가깝네. 이건 왜 좋게 나오지?
# # 5. 모든 결과를 소수점 둘째 자리까지 출력하시오
# print(f'{MAE:.2f} {MSE:.2f} {RMSE:.2f} {R2:.2f}')
# # 6. 실제 가격보다 10만큼 높은 예측과 100만큼 높은 예측이 있다면, MAE와 MSE 중 어느 지표가 큰 오차에 더 민감한지 그 이류를 설명하시오
# # MSE가 큰 오차에 더 민감합니다. 예측값과의 차이를 제곱해서 반영하기 때문입니다.

# 4단계. 작업형 제3유형 - 가설검정
import pandas as pd

df = pd.DataFrame({
    'A': [72, 75, 68, 80, 74, 71, 77, 73],
    'B': [82, 85, 78, 88, 84, 79, 81, 86]
})

# 아래부터 문제 풀이
from scipy.stats import ttest_ind

# 귀무가설: A집단과 B집단의 평균 점수는 학습 방식에 따라 차이가 없다
# 대립가설: A집단과 B집단의 평균 점수는 학습 방식에 따라 차이가 있다.

# 각 집단의 평균 계산
# mean() 활용
A_mean = df['A'].mean()
B_mean = df['B'].mean()

# 독립표본 t검정
stat, p_value = ttest_ind(df['A'], df['B'], equal_var=False)    # equal_var이 뭐지?

# 검정통계량과 p-value 출력
print(stat, p_value)
# if문을 사용하여 귀무가설 기각 여부 판단
if p_value < 0.05:
    print("귀무가설 기각")
else:
    print("귀무가설 기각 실패")
# 궁금한 점: stat은 무슨 의미가 있는 값이지?