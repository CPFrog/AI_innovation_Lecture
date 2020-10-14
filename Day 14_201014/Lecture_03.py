#%%
from selenium import webdriver
from bs4 import BeautifulSoup

import time
import re
import pandas as pd
import xlsxwriter
#%%
from selenium import webdriver
driver=webdriver.Edge('msedgedriver')
# %%
url = "https://finance.naver.com/sise/"
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'lxml')
soup.title
kospi = soup.find("span", id="KOSPI_now").text
kosdaq = soup.find("span", id="KOSPI_now").text
kospi_200 = soup.find("span", id="KPI200_now").text
print("코스피 지수 : {}".format(kospi))
print("코스닥 지수 : {}".format(kosdaq))
print("코스피200 지수 : {}".format(kospi_200))
pop_search = soup.find("ul", class_="lst_pop")
pop_search_li = pop_search.find_all("li")
pop_search_li[0]
all_stock = []
all_stock_url = []
code_all_num = []
for one in pop_search_li:
    stock = one.find("a").text
    price = one.find("span").text
    all_stock.append(stock)             # 종목명
    all_stock_url.append(price)         # 가격
    
    code = one.find("a").attrs
    code_num = code['onclick']         
    code_all = re.split(",", code_num)   
    code_all_num.append(code_all[2])    # 종목 코드

print( all_stock )
print( all_stock_url )
print( code_all_num )
# %%
dat = {"종목":all_stock, "가격":all_stock_url, "종목명":code_all_num}
pop_stock = pd.DataFrame(dat)
pop_stock.to_excel("stock.xlsx", sheet_name="Top10", index=False)
pop_search = soup.find("ul", class_="lst_major")
pop_search_li = pop_search.find_all("li")
pop_search_li[0]
all_stock = []
all_stock_price = []
code_all_num = []
for one in pop_search_li:
    stock = one.find("a").text
    price = one.find("span").text
    all_stock.append(stock)             # 종목명
    all_stock_price.append(price)         # 가격
    
print( all_stock )
print( all_stock_price )
dat = {"해외지수":all_stock, "지수":all_stock_price}
pop_stock = pd.DataFrame(dat)
pop_stock
# %%
dat1 = pd.read_excel("stock.xlsx", sheet_name="Top10")
writer = pd.ExcelWriter("stock.xlsx", engine='xlsxwriter')

dat1.to_excel(writer, sheet_name="Top10", index=False)
pop_stock.to_excel(writer, sheet_name="해외지수", index=False)

writer.save()  # 엑셀 파일 저장