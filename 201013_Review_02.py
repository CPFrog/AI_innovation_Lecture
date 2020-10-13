from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://finance.naver.com/sise"

#%%
page=urlopen(url)
soup=BeautifulSoup(page, "html.parser")
print(soup)
#%%
print(soup.find_all('span',id='KOSDAQ_now')[0].text)
print(soup.find_all('span',id='KOSPI_now')[0].text)
print(soup.find_all('span',id='KPI200_now')[0].text)

#%% 실습 1 : 코스피지수(거래량, 거래대금, 장중최고, 장중최저)

url_n='https://finance.naver.com/sise/sise_index.nhn?code=KOSPI'
page_n=urlopen(url_n)
soup_n=BeautifulSoup(page_n, 'html.parser')

quant=soup_n.find('td',id='quant').text
amount=soup_n.find('td',id='amount').text
high=soup_n.find('td',id='high_value').text
low=soup_n.find('td',id='low_value').text
print(quant, amount, high, low)
