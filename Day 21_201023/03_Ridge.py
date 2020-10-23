#%% 라이브러리 불러오기
import mglearn
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.linear_model import Ridge   # 릿지회귀
import pandas as pd
import numpy as np 
# %% 한글 설정
import matplotlib
from matplotlib import font_manager, rc
font_loc = "C:/Windows/Fonts/malgunbd.ttf"
font_name = font_manager.FontProperties(fname=font_loc).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

%matplotlib inline
# %%데이터 셋 준비 
boston = load_boston()  # 데이터 셋 불러오기
print(type(boston.target), type(boston.data))
print(boston.target.shape, boston.data.shape)

df_boston = pd.DataFrame(boston.data,columns=boston.feature_names)
df_boston['target'] = pd.Series(boston.target)
df_boston.head()
# %%
X=df_boston.loc[:, 'CRIM':'LSTAT']
y=boston['target']

print('정규화, 변수 확장 전의 데이터 셋 : ', X.shape, y.shape)
# %%
### 데이터 확장
### 모델 선택
### 모델 학습
### 모델 예측
### 결과 평가
#%% 데이터 확장
nor_x=MinMaxScaler().fit_transform(X)
print('입력의 최대, 최소값 :', np.min(nor_x), np.max(nor_x))

ex_X=PolynomialFeatures(degree=2,include_bias=False).fit_transform(nor_x)
print(ex_X.shape, y.shape)
# %%
from sklearn.linear_model import LinearRegression
# %%
X_train, X_test, y_train, y_test = train_test_split(ex_X, y, random_state=42)
lr=LinearRegression().fit(X_train, y_train)

print('학습용 데이터 셋 점수 : {:.2f}'.format(lr.score(X_train,y_train)))
print('시험용 데이터 셋 점수 : {:.2f}'.format(lr.score(X_test,y_test)))
# %%
# 위에서 차이가 많이 나는걸로 보아 과적합 일어남.
# Ridge 회귀 필요.
# %%
lr1=Ridge(alpha=1).fit(X_train,y_train)

print('학습용 데이터 셋 점수 : {:.2f}'.format(lr1.score(X_train,y_train)))
print('시험용 데이터 셋 점수 : {:.2f}'.format(lr1.score(X_test,y_test)))
# %% 실습 
# alpha를 0.0001, 0.001, 0.01, 0.1, 10, 100 으로 변경하며 구해보기
# alpha=0.001
# 학습용 점수(결정계수) : 
# 테스트 점수(결정계수) : 
# %%
ridge_p = [0.0001,  0.001, 0.01, 0.1, 10, 100]

for i in ridge_p:
    ridge = Ridge(alpha=i).fit(X_train, y_train)
    
    print("alpha : {}".format(i))
    print("훈련 데이터 세트 점수 : {:.2f}".format(ridge.score(X_train, y_train)))
    print("테스트 데이터 세트 점수 : {:.2f}".format(ridge.score(X_test, y_test)))
# %%
import matplotlib.pyplot as plt
%matplotlib inline
#%%
fig = plt.figure(figsize=(10,10))
plt.hlines(0,0, len(lr1.coef_))
plt.plot(lr1.coef_, 's', label="Ridge alpha=0.01")
plt.title('Ridge alpha=0.01')
# %%
