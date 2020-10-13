from bs4 import BeautifulSoup

html = """
<html>
<head><title> test site </title></head>
<p class='class1' align="left">test3</p>
<p class='class1'>test2</p>
<p id='p1'>오늘의 주가지수 1500</p>
<span class='class3'>span tag text</span>
<p class='class4'>test3</p>
</html>
"""

soup = BeautifulSoup(html, 'lxml')

print( list(soup.children)  )
print( list(soup.body.children)  )
#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup

url1 = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=171725&target=after&page=1"
page = urlopen(url1)
soup = BeautifulSoup(page, "html.parser")
comment_all = soup.find_all('td', class_='title')
print(comment_all)
#%% 갯수 확인
print(len(comment_all))
#%%
print(comment_all[0])
#%%
ch_td=list(comment_all[5].children)
print(ch_td[6].strip())
#%% 댓글 여러개 가져오기
comments = []
for comment in comment_all:
    temp=list(comment.children)
    result=temp[6].strip()
    comments.append(result)
    
print(comments)