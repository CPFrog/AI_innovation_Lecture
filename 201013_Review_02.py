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