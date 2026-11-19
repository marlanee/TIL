# 문제 3. 작업형 2유형 회귀 실전

"""
1. train.csv, test.csv를 불러오시오
2. id는 학습에서 지외하고 , amount를 예측 대상으로 설정하시오.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error, r2_score

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

train = train.drop(columns=['id'])
test = test.drop(columns=['id'])

X = train.drop(columns=['amount'])
y = train['amount']

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

mid = X_train.median(numeric_only=True)

X_train = X_train.fillna(mid)
X_val = X_val.fillna(mid)
test = test.fillna(mid)

X_train = pd.get_dummies(X_train)
X_val = pd.get_dummies(X_val)
test = pd.get_dummies(test)

X_val = X_val.reindex(
    columns=X_train.columns, fill_value=0
)
test = test.reindex(
    columns=X_train.columns, fill_value=0
)

model = RandomForestRegressor(random_state=42, n_estimators=100)

model.fit(X_train, y_train)

pred = model.predict(X_val)
test_pred = model.predict(test)

MAE = mean_absolute_error(y_val, pred)
MSE = mean_squared_error(y_val, pred)
RMSE = root_mean_squared_error(y_val, pred)
R2 = r2_score(y_val, pred)

print(MAE, MSE, RMSE, R2)

result = pd.DataFrame({"pred":test_pred})

result.to_csv("result.csv", index=False)

# 문제가 발생하면 당연히 힘들 것이다.
# 그러나, 정면으로 마주해야 한다.

# 문제 7. 작업형 3유형 실전 문제
from scipy.stats import ttest_ind, ttest_rel, shapiro, pearsonr
import pandas as pd
exam = pd.read_csv("exam.csv")

# ttest와 카이제곱 검정은 평균값으로 하는건가? 모두? 흠..
# 역시 아니었네. 표본 데이터 전체를 전달해야 되네.
A_after_mean = exam[exam['group'] == 'A']['after'].mean()

B_after_mean = exam[exam['group'] == 'B']['after'].mean()

stat, p = ttest_ind(A_after_mean, B_after_mean, equal_var=False)

before_mean = exam['before'].mean()
after_mean = exam['after'].mean()

ttest_rel(before_mean, after_mean)

shapiro(after_mean)

corr, p = pearsonr(after_mean)

print(f'{corr:.04f} {p:.04f}')