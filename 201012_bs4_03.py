from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://movie.naver.com/movie/running/current.nhn"

page=urlopen(url)
soup=BeautifulSoup(page, 'lxml')

print(soup.title)

#%%
ul_one = soup.find('ul', class_='lst_detail_t1')
print(ul_one.text)
#%%
a_all=ul_one.find_all('a')
print(a_all)
#%%
# dt, class:tit
# a -> text

li_all=ul_one.find_all('dt',class_='tit')
# print(li_all[0].text) << 데이터 확인용 출력
# print(li_all[1].text) << 데이터 확인용 출력

one_title=li_all[0].find('a')
print(one_title.text)

#%%

li_all=ul_one.find_all('dt',class_='tit')

for i in li_all:
    one_title=i.find('a').text
    print(one_title)

#%% 평점 정보 가져오기
# 1. 전체 가져오기
# 2. 하나씩 가져오는것 확인
# 3. for문으로 돌려보기

ul_one=soup.find('ul', class_='lst_detail_t1')
score_all=ul_one.find_all('span', class_='num')
print(score_all)

cnt=1;
for i in score_all:
    if cnt%2==0:
        print(i.text)
    cnt=cnt+1
#%% 실습 4-1 : 예매율 가져오기

for i in score_all:
    if cnt%2==0:
        print(i.text)
    cnt=cnt+1