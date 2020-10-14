#%% 네이버 데이터랩

filename='datalab_word.xlsx'
sheetname=input('시트명 입력 : ')
# %%
from selenium import webdriver
from bs4 import BeautifulSoup

driver=webdriver.Edge('msedgedriver')

# %%

url='https://datalab.naver.com/keyword/realtimeList.naver'
driver.get(url)
# %%
xpath_10='//*[@id="content"]/div/div[2]/div[1]/div[2]/div/div/div/ul/li[1]/a'
sel_10=driver.find_element_by_xpath(xpath_10)
sel_10.click()
# %%
html=driver.page_source
soup=BeautifulSoup(html, 'lxml')
soup.title
#%%
age_10=soup.find_all('span', class_='item_title')
# %%
pop_10=[]
for i in age_10:
    text=i
    pop_10.append(text)

print(pop_10)
# %% 실습 3-2
# 20대 키워드 불러오기
xpath_20='//*[@id="content"]/div/div[2]/div[1]/div[2]/div/div/div/ul/li[2]/a'
#%%
import time
# %%
base_xpath1='//*[@id="content"]/div/div[2]/div[1]/div[2]/div/div/div/ul/li['
base_xpath2=']/a'

all_word=[]

for i in range(1,7):
    all_xpath=base_xpath1+str(i)+base_xpath2
    sel_btn=driver.find_element_by_xpath(all_xpath)
    sel_btn.click()

    soup=BeautifulSoup(driver.page_source,'lxml')
    age_data=soup.find_all('span',class_='item_title')

    pop_10=[]
    for i in age_data:
        text=i.text
        pop_10.append(text)

    time.sleep(0.5)
    all_word.append(pop_10)
    print(pop_10)
# %%
dict_val = (
    '10대 :', all_word[0],
    '20대 :', all_word[1],
    '30대 :', all_word[2],
    '40대 :', all_word[3],
    '50대 :', all_word[4],
    '전체 :', all_word[5],
)
# %%
