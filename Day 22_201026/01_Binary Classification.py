#%% 한글
from sklearn.model_selection import train_test_split
import matplotlib
from matplotlib import font_manager, rc
font_loc = "C:/Windows/Fonts/malgunbd.ttf"
font_name = font_manager.FontProperties(fname=font_loc).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False
# %% 라이브러리 호출
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
import mglearn
import matplotlib.pyplot as plt 
# %%
X, y = mglearn.datasets.make_forge()
print(X.shape, y.shape)
print(X[:5], y[:5])  # 앞에서부터 5개까지의 출력
#%%
# a=[1,2,3]
# b=[4,5,6]

## zip -> C++의 pair 개념과 비슷함.
# for i,j in zip(a,b):
#    print(i,j)
# %%
fig, axes = plt.subplots(1, 2, figsize=(10, 3))
for model, ax in zip([LinearSVC(), LogisticRegression()], axes):
    clf = model.fit(X, y)
    mglearn.plots.plot_2d_separator(
        clf, X, fill=False, eps=0.5, ax=ax, alpha=0.7)
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
    ax.set_title(clf. __class__.__name__)
    ax.set_xlabel("특성 0")
    ax.set_ylabel("특성 1")
axes[0].legend()
# %% C 값에 따른 그래프

mglearn.plots.plot_linear_svc_regularization()

# C 값은 클수록 규제를 안하고 릿지 랏소 alpha 값이 클수록 규제가 큼
# C가 작을수록 규제가 강함. -> 릿지, 랏소 alpha 값이 작을수록 원래 회귀모형과 비슷함.
# %%
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

X = cancer.data
y = cancer.target


X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=42)
# stratify -> 데이터 불균형 없애주는 역할
# %%
# C의 기본값은 1
logreg = LogisticRegression(C=1).fit(X_train, y_train)

print("훈련 세트 점수 : {:.3f}".format(logreg.score(X_train, y_train)))
print("테스트 세트 점수 : {:.3f}".format(logreg.score(X_test, y_test)))
# %% 실습 : C 값을 0.001, 0.01, 10, 100 설정하고 score 값 구하기

lr001=LogisticRegression(C=0.001).fit(X_train, y_train)

print("훈련 세트 점수 : {:.3f}".format(lr001.score(X_train, y_train)))
print("테스트 세트 점수 : {:.3f}".format(lr001.score(X_test, y_test)))

lr01=LogisticRegression(C=0.01).fit(X_train, y_train)

print("훈련 세트 점수 : {:.3f}".format(lr01.score(X_train, y_train)))
print("테스트 세트 점수 : {:.3f}".format(lr01.score(X_test, y_test)))

lr10=LogisticRegression(C=10).fit(X_train, y_train)

print("훈련 세트 점수 : {:.3f}".format(lr10.score(X_train, y_train)))
print("테스트 세트 점수 : {:.3f}".format(lr10.score(X_test, y_test)))

lr100=LogisticRegression(C=100).fit(X_train, y_train)

print("훈련 세트 점수 : {:.3f}".format(lr100.score(X_train, y_train)))
print("테스트 세트 점수 : {:.3f}".format(lr100.score(X_test, y_test)))

#%% 심화 : 위의 실습을 for문으로 코드간소화.
a=[0.001, 0.01, 10, 100]
for i in a:
    lr=LogisticRegression(C=i).fit(X_train,y_train)
    print("C 가 {} 일때".format(i))
    print("훈련 세트 점수 : {:.3f}".format(lr.score(X_train, y_train)))
    print("테스트 세트 점수 : {:.3f} \n".format(lr.score(X_test, y_test)))
# %% 위의 데이터 시각화
plt.plot(lr001.coef_.T,'^', label='C=0.001')
plt.plot(lr01.coef_.T,'^', label='C=0.01')
plt.plot(logreg.coef_.T, '^', label='C=1')
plt.plot(lr10.coef_.T,'o', label='C=0.10')
plt.plot(lr100.coef_.T, 'v', label='C=100')