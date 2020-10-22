# 오늘 수업은 프로젝트 발표 및 이론수업이 주로 이뤄져, 코드가 그리 많지 않음을 참고.
#%% Intro : 파이썬 라이브러리
# pandas : 데이터 처리, 읽기, 쓰기 등
# matplotlib, seaborn, plotly, folium
# numpy : 배열, 선형대수 처리
# scipy : 과학 계산용 함수, 고성능 선형대수, 함수최적화, 희소행렬
# os : 운영체제 관련 폴더생성, 파일 찾기 등.
# sklearn(scikit-learn) : 머신러닝 관련
# tensorflow(구글), pytorch(페북), keras(구글), mx-net(아마존)
# mglearn (책 저자분이 그래프 설명을 위해 직접 만든 것)

#%% 라이브러리 불러오기
import pandas as pd
import tensorflow as tf
import keras
import numpy as np
import sys
import mglearn
import matplotlib as mpl
import matplotlib.pyplot as plt 
import scipy as sp 
import seaborn as sns
# %%
from IPython.display import display, Image
# %% 버전 확인
print('파이선 버전 : ', sys.version)
print('판다스 버전 : ', pd.__version__)
print('matplotlib 버전 : ', mpl.__version__)
print('seaborn 버전 : ', sns.__version__)
# %% 데이터 : 붓꽃
# 종류 : setosa, versicolor, virginica
# 데이터 내용 : 붓꽃의 꽃잎과 꽃받침
# 우리가 해결하려고 하는 문제 : 데이터를 주고 붓꽃의 종류 예측하기
# %% 데이터 준비
from sklearn.datasets import load_iris
iris = load_iris()

# iris 데이터 - 딕셔너리 (키:값)
print(iris.keys())
# └ dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])

# %% iris 데이터 셋의 행열 확인
print( iris['data'].shape )
print( iris['feature_names'])
print( iris['data'][:5])      # 5개의 데이터 확인
print( iris['target_names'][:5]) 
print( iris['target'][:5]) 

# iris 데이터 설명
# data : 꽃잎의 너비길이, 꽃받침의 너비와 길이 (4개 변수, feature) : 150개
# feature_names : data의 값이 갖는 이름
# target : 꽃의 종류 (0,1,2)
# target_names : 꽃잎 종류의 이름 (0:setosa, 1 : versicolor, 2 : verginica)
# DESCR : 이 데이터 셋의 설명
# %% iris 데이터 셋의 크기 (행, 열)
print(iris['target'].shape)
# %% 데이터를 나누기
# train.csv, test.csv
# train : 학습(머신에 공부시킬 데이터)
# test : 예측을 위한 데이터
# 총 150개의 iris 데이터(data, target)를 나눠준다
# 학습용, 테스트용
# %%
from sklearn.model_selection import train_test_split
# train_test_split(입력, 출력)

all_x=iris['data']
all_y=iris['target']

x_train, x_test, y_train, y_test = train_test_split(all_x, all_y, random_state=42)
# 실행때마다 랜덤하게 뽑히기 때문에 random_state 로 시드값 줌
# %%
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

# 강사님이 변수에 x를 대문자로 쓴 이유 : 2차원이라..
# 보통 1차원(벡터)은 소문자, 2차원 이상(행렬)은 대문자로 나타내는게 암묵적 룰.
# 다음시간부턴 내 코드도 통일하는걸로.
# %% 모델선택, 모델학습, 모델을 이용한 예측, 평가
from sklearn.neighbors import KNeighborsClassifier
# %% 모델선택
knn=KNeighborsClassifier()
# %% 모델 학습(입력, 출력)
knn.fit(x_train, y_train)

# %% 모델을 이용한 예측 - [모델이름].predict(새로운 데이터(입력))
pred = knn.predict(x_test)
print(pred)
# %% 평가 - 원래 답(y_test), 예측한 값(pred)
# 맞힌 개수/전체 개수(정확도 비율)
print(sum(pred==y_test)/len(pred))
# %% 실습. seed 값 변경하고, 데이터를 50 : 50으로 나눠 학습
x2_train, x2_test, y2_train, y2_test = train_test_split(all_x, all_y, random_state=11,test_size=0.5, train_size=0.5)

knn2=KNeighborsClassifier()
knn2.fit(x2_train,y2_train)

pred2=knn2.predict(x2_test)
print(sum(pred2==y2_test)/len(pred2))