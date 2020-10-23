#%% 선형모델
# 특성(feature) 하나이면 직선
# 특성(feature) 두개이면 평면
# 여러개는 초평면
# %% 학습을 통해 정해지는 값
# 회귀 계수 특성이 하나면 y=w1*x1+b
# 회위 계수 특성이 두개면 y=w1*x1+w2*x2+b ...
# 정해지는 값은 w1,w2,...,b
# %%
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
# %%
boston = load_boston()
X=boston.data
y=boston.target

print(X.shape, y.shape)
print(boston['feature_names'])
# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
# %%
model=LinearRegression()
model.fit(X_train, y_train)
pred=model.predict(X_test)
pred[:5]
# %%
import pandas as pd 
import numpy as np 
# %%
dict_dat={'실제값' : y_test, '예측값' : pred, '오차' : y_test-pred, '오차절대값' : np.abs(y_test-pred), '오차제곱':(y_test-pred)**2}

dat=pd.DataFrame(dict_dat)
dat
#%%
print(dat.shape)
# %% MAE 구하기 
# MAE란 = 각 데이터의 오차 절대값의 합을 구하고 이를 데이터 개수로 나눠준 것
np.sum(dat['오차절대값'])/dat.shape[0]
# np.mean(dat['오차절대값'])
# %% MSE 구하기
# MSE : 각 데이터의 오차제곱 의 평균
np.mean(dat['오차제곱'])
# %% RMSE 구하기
# RMSE : MSE 값의 분포 (root 씌움)
mse=np.mean(dat['오차제곱'])
rmse1=np.sqrt(mse)
rmse2=mse**.5

print(rmse1, rmse2)
# %% 실습 : 데이터를 9:1, 8:2, 7:3 으로 했을 때 RMSE 값 구하기

# %% 모델의 score 메소드를 이용한다
print('학습용 스코어 : ',model.score(X_train, y_train))
print('시험용 스코어 : ',model.score(X_test, y_test))
# %% 회귀 모델에서 score는 결정개수라는 것을 의미한다.
# 결정계수는 회귀모델에서 모델의 적합도를 의미하는 것으로 0~1사이의 값을 가짐
# 1에 가까우면 가까울수록 이 모델은 좋다고 볼 수 있다.