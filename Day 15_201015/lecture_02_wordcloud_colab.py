# -*- coding: utf-8 -*-
"""Lecture_02_Wordcloud_colab

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cEhGyahjQwxSsYWK9ISpjfDuRuT5bEbo

### 사전 작업
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import nltk
import numpy as np

!apt-get update -qq
!apt-get install fonts-nanum* -qq

font_name=fm.FontProperties(fname= '/usr/share/fonts/truetype/nanum/NanumGothic.ttf', size=10).get_name()
print(font_name)
plt.rc('font', family=font_name)

fm._rebuild()

from wordcloud import WordCloud, STOPWORDS
from PIL import Image

text = open('alice.txt').read()
text

"""### 파이썬 자료형 집합에 대해 알아보기
* 중복 제거
"""

# 불용어 단어 추가
stopwords = set(STOPWORDS)
stopwords.add('said')
stopwords

"""### 앨리스 이미지 확인"""

alice_mask=np.array(Image.open('alice_color.png'))
alice_mask[0]

wc = WordCloud( background_color='white',   # 배경색
               max_words=2000,              # 최대 표시 단어
               mask=alice_mask,             # 마스크 이미지
               contour_width=3,             # 외곽선 
               contour_color="steelblue" )  # 색
wc.generate(text)
wc.words_

plt.figure(figsize=(15,8))  # 크기
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off') # x,y축 안보이게
plt.show()

"""### 위에서 생성한 wc 데이터를 이용해 그래프에 표시"""

plt.figure(figsize=(15,8))
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()

"""### 영화 댓글 시각화
* 분노의 질주 댓글 분석
"""

