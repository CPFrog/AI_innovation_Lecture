# 1. 데이터 다운
# 2. 데이터를 이용하여 머신러닝 모델을 만들고
#   학습한 모델을 이용하여 새로운 데이터의 독이 있는지 없는지 예측

# import urllib.request as req

# local = "mushroom.csv"
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
# req.urlretrieve(url, local)
# print('Successfully downloaded.')

# 모델 생성
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

mush = pd.read_csv('mushroom.csv', header=None)
# print(mush)

from sklearn import preprocessing

encoder_le = preprocessing.LabelEncoder()
mush['label'] = encoder_le.fit_transform(mush.iloc[:, 0])
# print(mush)

for i in range(1, 23, 1):
    mush['col' + str(i)] = encoder_le.fit_transform(mush.iloc[:, i])

# print(mush)

x = mush.loc[:, 'col1':'col22']
y = mush['label']

print(x.shape, y.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, test_size=.5)

print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

model = RandomForestClassifier()
model.fit(x_train, y_train)

predict = model.predict(x_test)

print(len(predict))
print(predict)


import numpy as np

print(predict == y_test.values)
print(np.sum(predict == y_test.values))
