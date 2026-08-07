import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# 1. 11차원 데이터 세트 생성 (독립변수 10개 + 종속변수 1개 = 총 11차원)
X_data, y_data = make_regression(n_samples=300, n_features=10, noise=15, random_state=42)
feature_names = [f'X{i+1}' for i in range(10)]

# 2. 11차원 다중선형회귀 모델 학습
model = LinearRegression()
model.fit(X_data, y_data)
y_pred = model.predict(X_data)

# 3. 11차원 초평면 종합 시각화 대시보드
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# [관점 1] 11차원을 2차원으로 압축: 실제값 vs 예측값
axes[0, 0].scatter(y_data, y_pred, alpha=0.6, color='#2b5c8f')
axes[0, 0].plot([y_data.min(), y_data.max()], [y_data.min(), y_data.max()], 'r--', lw=2)
axes[0, 0].set_title("1. Actual vs Predicted (11D -> 2D Projection)")
axes[0, 0].set_xlabel("Actual Y")
axes[0, 0].set_ylabel("Predicted Y (from 11D Model)")
axes[0, 0].grid(True, linestyle='--', alpha=0.5)

# [관점 2] 11차원 초평면의 축별 기울기 (계수 크기)
coef_df = pd.DataFrame({'Feature': feature_names, 'Coefficient': model.coef_})
coef_df = coef_df.sort_values(by='Coefficient', ascending=False)
sns.barplot(data=coef_df, x='Coefficient', y='Feature', ax=axes[0, 1], palette='Blues_r')
axes[0, 1].set_title("2. 11D Hyperplane Slopes per Axis (Coefficients)")
axes[0, 1].grid(True, linestyle='--', alpha=0.5)

# [관점 3] 가장 영향력 높은 축(X 축 중 하나) 단면 단층 관찰
top_feature_idx = np.argmax(np.abs(model.coef_))
axes[1, 0].scatter(X_data[:, top_feature_idx], y_data, alpha=0.4, color='gray', label='Data Points')
# 다른 변수를 평균으로 고정한 단면 기울기
x_range = np.linspace(X_data[:, top_feature_idx].min(), X_data[:, top_feature_idx].max(), 100)
y_section = model.coef_[top_feature_idx] * x_range + model.intercept_
axes[1, 0].plot(x_range, y_section, color='red', lw=2, label=f'Slope of {feature_names[top_feature_idx]}')
axes[1, 0].set_title(f"3. Cross-section View along {feature_names[top_feature_idx]} Axis")
axes[1, 0].set_xlabel(feature_names[top_feature_idx])
axes[1, 0].set_ylabel("Y")
axes[1, 0].legend()
axes[1, 0].grid(True, linestyle='--', alpha=0.5)

# [관점 4] 잔차(오차) 분포 관찰
residuals = y_data - y_pred
axes[1, 1].scatter(y_pred, residuals, alpha=0.6, color='#8f2b5c')
axes[1, 1].axhline(0, color='black', linestyle='--')
axes[1, 1].set_title("4. Residuals Plot (Error Spread)")
axes[1, 1].set_xlabel("Predicted Y")
axes[1, 1].set_ylabel("Residual (Error)")
axes[1, 1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()