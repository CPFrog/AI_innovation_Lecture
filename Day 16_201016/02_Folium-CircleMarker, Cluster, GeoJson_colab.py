# -*- coding: utf-8 -*-
"""201016_Lecture_02_Folium.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MoJBVL0QQdTYrVH61_ZJXL3Dy1yKwRtv
"""

import folium

pip install git+https://github.com/python-visualization/branca.git@master

"""### CircleMarker 이용"""

m = folium.Map(
    location=[37.5466423,126.9092281],
    zoom_start=15
)

folium.CircleMarker(
    location=[37.5466423,126.9092281],
    radius = 100, color = '#ffffgg', fill_color='#fffggg', popup = '양화진',
    icon = folium.Icon(color='red', icon='star')  # 아이콘 
).add_to(m)

m

from folium import plugins

"""### Marker를 군집화 시키기 - MarkerCluster"""

import numpy as np
import os

N=100

data=np.array(
    [
     np.random.uniform(low=35, high=60, size=N),
     np.random.uniform(low=-12, high=30, size=N)
    ]
).T

print(data.shape) # 행열 크기 (행, 열)
print(data.ndim) # 차원

newdata=data.T
print(newdata.shape)
print(newdata.ndim)

popups=[str(i) for i in range(N)]

m=folium.Map([45, 3], zoom_start=4)
plugins.MarkerCluster(data, popups=popups).add_to(m) 
m.save(os.path.join('.', 'Plugins_1.html')) 

m

"""### GeoJson 행정 구역 데이터"""

!ls

import folium

m=folium.Map(location=[37.5838699,127.0565831])

import json
with open('seoul_municipalities_geo.json',mode='rt',encoding='utf-8') as f:
    geo = json.loads(f.read())
    f.close()
  
folium.GeoJson(geo, name='seoul_municipalities').add_to(m)

m.save('map.html')
m
