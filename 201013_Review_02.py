from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://finance.naver.com/sise"

#%%
page=urlopen(url)
soup=BeautifulSoup(page, "html.parser")