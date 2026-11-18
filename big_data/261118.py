# 빅분기 시험 D-10. 아이고... 
# 시작 시간: 13:50
# 1단계. 작업형 2유형 - 이진 분류
# 실전 문제 1. 고객의 대출 연체 여부 예측
"""
목표: 
    1. train, test 데이터프레임이 주어진다. 예측 목표는 test라는 column, 평가 지표는 ROC-AUC, 
    2. 모델은 RandomForestClassifier
문제: 
    1. 필요한 라이브러리와 함수 import
    2. id열 제거
    3. 독립변수 x와 종속변수 y 분리
    4. 훈련 데이터와 검증 데이터를 8:2로 분리
    5. 클래스 비율 유지 및 random_state=42 설정
"""

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

train = train.drop(columns=['id'])
test = test.drop(columns=['id'])

X = train.drop(columns=['target'])
y = train['target']

# 나는 train 데이터를 X_train, X_test, y_train, y_test로 나누는 것은 배웠다. 
# 그런데 test 데이터까지 주어지면 어떻게 활용해야 할까?
# 아! 굳이 나눌 필요가 없지 않나. 나중에 검증할 때 사용하는거 아닌가?

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# test는 정답이 없기 때문에, train 데이터를 분할해서 X_train, X_val로 나누고 훈련 및 검증한다.

# 문제 1-2. 결측치 처리 및 인코딩. 14:11
"""
목표: 
    1. 수치형 변수의 결측치를 중앙값으로 처리하세요.
    2. 범주형 변수는 pd.get_dummies()로 인코딩하세요
    3. 세 데이터프레임의 열 구성과 순서를 일치시키세요.
    4. 데이터 누수가 발생하지 않도록 하세요
"""

train_median = X_train.median(numeric_only=True)
X_train = X_train.fillna(train_median)  # 어? 이상하다. Dataframe의 열을 지정하지 않아도 결측치 처리가 가능한가?
X_val = X_val.fillna(train_median)  # 가능하다. train_medain이 열 이름을 인덱스로 가지는 Series이기 때문이다.
test = test.fillna(train_median)    # !!!! test 데이터도 결측치 처리를 해야 한다. 물론 데이터 누수 없게끔.

X_train = pd.get_dummies(X_train, dtype=int)    # 하 이거 아닌 것 같은데?
X_val = pd.get_dummies(X_val, dtype=int)    # 맞단다. 허허. 인코딩은 별 거 없네.
test = pd.get_dummies(test, dtype=int)

# X_train을 제외한 Dataframe은 총 두 개. test는 그렇다 치고, y_train도 해야되나? 
# 하지만 데이터를 분할하는 과정에서 X_train에 들어간 요소가 y_train에 없을수도 있지 않나?
X_val = X_val.reindex(
    columns=X_train.columns, fill_value=0
)
test = test.reindex(
    columns=X_train.columns, fill_value=0
)

# 문제 1-3. 모델 학습 및 성능 평가. 14:50 / 14:59
"""
1. RandomForestClassifier 모델 생성
2. 의사결정나무 100개, random_state=42 설정
3. 훈련 데이터를 활용한 모델 학습
4. 검증 데이터의 연체 확률(클래스 1의 확률 예측)
5. ROC-AUC 점수 계산 및 출력
"""

model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X_train, y_train)

# from spicy import predict_proba # 이건 진짜 뭐지? spicy는 진짜 아닌 것 같은데
# predict_proba는 별도로 import 하는 함수가 아니라고 한다. 학습된 모델의 메서드라고 한다.

proba = model.predict_proba(X_val)[:, 1]  # 슬라이싱은 정확한가?

score = roc_auc_score(y_val, proba) # ROC-AUC에 proba가 들어가는 것 같긴 한데.. y_val이 들어가는게 맞나?
# 맞다.


# 문제 1-4. 최종 예측 및 csv 제출. 15:04 / 15:11 힌트 참조
"""
1. test의 클래스 1에 대한 연체 확률을 예측하세요.
2. 예측 결과를 pred라는 열을 가진 DataFrame으로 생성하세요
3. result.csv 라는 이름으로 저장하세요
4. CSV 파일에 인덱스가 포함되지 않도록 하세요
"""

# 클래스 1? 그게 뭐지? 클래스는 예측해야 하는 값 아닌가? 그게 연체 확률 아니야? 연체 확률에 대한 연체 확률 예측?
# 클래스 1: 연체함. 클래스 1의 확률: 해당 고객이 연체할 것으로 모델이 추정한 확률. 그렇군.
test_proba = model.predict_proba(test)[:, 1]    # 연체라는 사건이 발생한 확률 구하기. 정답

# 오잉? 저걸 DataFrame으로 만들라고? 뭐 그런 메서드나 함수가 있나?
result = pd.DataFrame({"pred": test_proba})  # 딕셔너리에 담네. 희한하네 아주. 열 이름과 데이터 동시 지정

result.to_csv("result.csv", index=False)    # 아무리 봐도 아니긴 한데..

# 인덱스를 어떤 방법으로 제외시켜야 되는거야? -> index=False

# 문제 1-4 재시험.
"""
1. 시험용 데이터를 model로 클래스 1의 확률로 예측해서 probability라는 열 이름으로 만들어서 submission.csv로 제출. 인덱스 없이.
"""

test_proba = model.predict_proba(test)[:, 1]

submission = pd.DataFrame({'probability': test_proba})

submission.to_csv("submission.csv", index=False)    # 궁금한 점. .csv가 아닌 .txt로 하면 메모장처럼 저장되나?

# 문제 1-5. 이진 분류 전체 과정 백지 구현
# 실전 모의시험
"""
1. CSV 파일 불러오기
2. 불필요한 변수 제거
3. 독립변수와 종속변수 분리 # 이게 target 기준으로 분리하는거 맞지?
4. 훈련, 검증 데이터 8:2분할 및 클래스 비율 유지
5. 수치형 결측치 중앙값 처리
6. 범주형 변수 원핫 인코딩 및 열 일치
7. RandomForestClassifier 사용 (나무 100개)
8. random_state=42
9. ROC-AUC를 활용한 모델 성능 검증 및 출력
10. 실제 시험용 데이터의 연체 확률 예측
11. pred라는 열 이름으로 result.csv 제출
"""
import pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

train = pd.read_csv("train.csv")    # 엥 이게 맞나?
test = pd.read_csv("test.csv")  # pd 붙여야한다.

train = train.drop(columns=['id'])
test = test.drop(columns=['id'])

X = train.drop(columns=['target'])
y = train['target']

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

train_median = X_train.median(numeric_only=True)

X_train = X_train.fillna(train_median)
X_val = X_val.fillna(train_median)
test = test.fillna(train_median)

X_train = pd.get_dummies(X_train, dtype=int)  # 얘는 등호로 재할당 안 해도 되나?
X_val = pd.get_dummies(X_val, dtype=int)    # 아니, 반드시 재할당 해야한다. 원-핫 인코딩 말이야.
test = pd.get_dummies(test, dtype=int)

X_val = X_val.reindex(
    columns=X_train.columns, fill_value=0
)
test = test.reindex(
    columns=X_train.columns, fill_value=0
)

model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X_train, y_train)

train_proba = model.predict_proba(X_val)[:, 1]

score = roc_auc_score(y_val, train_proba)
print(score)

test_proba = model.predict_proba(test)[:, 1]

result = pd.DataFrame({"pred": test_proba})

result.to_csv("result.csv", index=False)