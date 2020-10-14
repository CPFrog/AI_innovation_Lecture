#%%
from selenium import webdriver

driver = webdriver.Edge()

# xpath : //*[@id="query"]
# 버튼의 xpath : //*[@id="search_btn"]
sel_xpath = driver.find_element_by_xpath('//*[@id="query"]')
sel_btn = driver.find_element_by_xpath('//*[@id="search_btn"]')

#%%
print(sel_xpath)
print(sel_btn)

#%%
sel_xpath.send_keys('미세먼지')

#%%
sel_btn.click()

#%%
url='https://pythonstart.github.io/web/'
driver.get(url)

#%%
sel_id=driver.find_element_by_id('rank')
print(sel_id)

sel_id.text

sel_id.tag_name

sel_id.click()
#%% 실습1. 여러개 가져오기
# a 태그의 텍스트 전체 가져오기
# find_elements_by_tag_name('태그명')
# for문을 돌려서 하나씩 텍스트 출력