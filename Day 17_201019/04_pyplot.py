#%%
import cufflinks as cf
import plotly as py
import pandas as pd
import numpy as np
#%% 오프라인 모드에서도 인터렉티브한 그래픽을 가능하도록 하기
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)
cf.go_offline()

#%% 데이터 생성
df = pd.DataFrame(np.random.randn(100,4), # 100개 4개 컬럼
 columns='A B C D'.split())
print(df.shape)
df.head()
df2 = pd.DataFrame({'items':['bag','apple','cap'],'Values':[32,43,50,]})
df2
df.iplot()
df.iplot(kind='scatter', x='A',y='B',mode='markers',size=20)
df2.iplot(kind='bar', x='items', y='Values')
# %%
df = pd.DataFrame(np.random.rand(10,4),
                  columns=['A', 'B', 'C', 'D'])
df.head()
df['A'].iplot(kind='bar')
# %%
df.iplot(kind='barh', barmode='stack')
df.iplot(kind='box')
# %%
df3 = pd.DataFrame({'x':[1,2,3,4,5],
 'y':[10,20,30,40,60],
 'z':[5,4,3,2,1]})
df3
# %%
df3.iplot(kind='surface',colorscale='rdylbu')
# %%
df = cf.datagen.lines()
df.head()
# %%
themes = cf.getThemes()
themes
# %%
data = pd.Series(range(10))
for theme in themes:
 data.iplot(kind='bar', theme=theme, title=theme)
# %%
train=pd.read_csv('train.csv')
train
# %%

# %% 승선항 시각화
train.iplot(kind='bar', x='Embarked',y='Survived')
# 승선항은 S, C, Q가 있음
# S 승선자 다수가 살았음
# 왜 S에 승선한 사람이 많이 살았는가를 데이터로 추측