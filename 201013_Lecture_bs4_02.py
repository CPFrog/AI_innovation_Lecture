# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

my_stock=['삼성전자', '카카오', '유한양행', '네이버']
my_stock_code=['005930', '035720', '000100', '035420']

base_url='https://finance.naver.com/item/main.nhn?code='

com=[] # 회사 명
price_c=[] #가격

cnt=0
for code in my_stock_code:
    all_url=base_url+code
    page=urlopen(all_url)
    soup=BeautifulSoup(page, 'lxml')
    
    ## 현재가
    tmp=soup.find('p',class_='no_today')
    price=tmp.find('span',class_='blind').text
    
    com.append(my_stock[cnt])
    price_c.append(price)
    
    cnt+=1
    
print(com)
print(code_p)
print(price_c)

#%%
import pandas as pd

dic={'회사' : com,
     '코드' : code_p,
     '현재가' : price_c}

dat=pd.DataFrame(dic)
print(dat)

# 엑셀파일화
dat.to_excel("stock.xlsx", index=False)

# csv a,b,c
dat.to_csv("stock.csv", index=False)