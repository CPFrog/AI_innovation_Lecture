#%%
import mglearn
import matplotlib.pyplot as plt 
import pandas as pd

# %%
mglearn.plots.plot_knn_regression(n_neighbors=1)
# %% 유방암 데이터 셋
# 위스콘신 유방암 데이터 셋
# 입력 : 569개, 30개의 열
# 출력 : 악성(malignant), 양성(benign) (0,1)
# %%
from sklearn.datasets import load_breast_cancer
# %%
cancer=load_breast_cancer()
cancer.keys()
# %%
# data : 입력 569개, 출력 30개 열
# target : 출력 (악성, 양성) 0,1
# %%
print(cancer['target_names'])
print(cancer['target'][:20])

print(cancer['feature_names'])
print(cancer['data'][:1])
# %% 
# 데이터 나누기
# 모델 선택후 훈련
# 훈련된 모델로 예측 및 정확도 확인

from sklearn.model_selection import train_test_split

X=cancer.data
y=cancer.target

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=cancer.target,random_state=42)
# %% target의 확인
print((y_train==1).sum(), (y_train==0).sum())
print((y_test==1).sum(), (y_test==0).sum())
print(267/(267+90),159/(159+53))
print(90/(26+90),53/(159+53))
# %%
from sklearn.neighbors import KNeighborsClassifier
# %%
model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
pred=model.predict(X_test)
pred
# %%
(pred==y_test).sum()/len(pred)
# %%
# k=1, 0.9231
# k=3, 0.9231
# k=5, 0.9231
# k=7, 0.930
# %%
acc_tr=model.score(X_train, y_train)
acc_test=model.score(X_test, y_test)

print('k : {}'.format(3))
print('훈련 데이터셋 정확도 : {:.2f}'.format(acc_tr))
print('테스트 데이터셋 정확도 : {:.2f}'.format(acc_test))

# %%
tr_acc=[]
test_acc=[]
k_nums=range(1,22,2)  #1,3,5,...,21

max=1
max_ind=0
for n in k_nums:
    # 모델 선택 및 학습
    model=KNeighborsClassifier(n)
    model.fit(X_train,y_train)

    # 정확도 구하기
    acc_tr=model.score(X_train, y_train)
    acc_test=model.score(X_test, y_test)

    # 정확도 값 저장
    tr_acc.append(acc_tr)
    test_acc.append(acc_test)

    print('k :', n)
    print('훈련 데이터셋 정확도 : {:.3f}'.format(acc_tr))
    print('테스트 데이터셋 정확도 : {:.3f}'.format(acc_test))
    dif=acc_tr-acc_test
    if dif<0 : dif=dif*-1
    if max>acc_tr-acc_test : 
        max_ind=n
        max=
print('가장 좋은 모델 :', max_ind)