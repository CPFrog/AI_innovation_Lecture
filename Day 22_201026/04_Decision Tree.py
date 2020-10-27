# %% 한글 설정

import matplotlib
from matplotlib import font_manager, rc
font_loc = "C:/Windows/Fonts/malgunbd.ttf"
font_name = font_manager.FontProperties(fname=font_loc).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False
# %%
import matplotlib.pyplot as plt 
import mglearn
# %%
plt.figure(figsize=(10,10))
mglearn.plots.plot_animal_tree()
# %%
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

import seaborn as sns
# %%
cancer = load_breast_cancer()

all_X=cancer.data
all_Y=cancer.target
# %%
X_train, X_test, y_train, y_test = train_test_split(all_X, all_Y, stratify=cancer.target, test_size=0.3, random_state=77)

tree = DecisionTreeClassifier()
tree
#%% 학습 훈련, score 확인
tree.fit(X_train, y_train)

print("학습용 데이터 셋 정확도 : {:.3f}".format(tree.score(X_train, y_train)))
print("테스트 데이터 셋 정확도 : {:.3f}".format(tree.score(X_test, y_test)))
# %%
from sklearn.tree import export_graphviz
export_graphviz(tree, out_file="tree.dot", 
                class_names=['악성', '양성'],
                feature_names = cancer.feature_names, 
                impurity = False,
                filled=True)
# %%
import graphviz
with open("tree.dot", encoding='UTF-8') as f:
  dot_graph = f.read()
display(graphviz.Source(dot_graph))
# %% 트리모델의 특성(feature)의 중요도를 막대그래프로 표현해주는 함수
import numpy as np

def plot_feature_imp_cancer(model):
  n_features=cancer.data.shape[1]
  imp=model.feature_importances_

  plt.barh(range(n_features),imp,align='center')
  plt.yticks(np.arange(n_features, cancer.feature_names)) # y축 - 특징이름

  plt.xlabel('특성중요도')
  plt.ylabel('특성')
  plt.ylim(-1,n_features)