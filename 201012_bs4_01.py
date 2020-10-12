# -*- coding: utf-8 -*-

#%%
from bs4 import BeautifulSoup

page = open('201012_review.html', 'r', encoding='utf-8').read()
print(page)

soup=BeautifulSoup(page,"html.parser")
print(soup)

#%%
# 헤드라인1을 가져오기

data=soup.find("h1")
print(data.text)

# 단락1 정보 가져오기
p1=soup.find("p")
print(p1)

#%% 실습 2-1 링크 정보 가져오기
link_txt=soup.find('a')
print(link_txt.text)