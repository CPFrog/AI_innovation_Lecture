#%%
from selenium import webdriver

driver = webdriver.Edge('./msedgedriver')

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

ele_a=driver.find_elements_by_tag_name('a')
for one in ele_a:
    print(one.text)
    
# %%
selected_name = driver.find_element_by_name('text_get')
print(selected_name)     # WebElement 객체 확인
print(selected_name.tag_name)  # 태그 이름 확인 

# find_elements_by_name 이용해 보기
# name이 'q'인것이 하나이기에 길이가 1인 리스트가 반환됨.
selected_names = driver.find_elements_by_name('link_get')
print(len(selected_names))
# %% selector를 이용한 접근
# find_element by_css_selector
# find_elements_by_css_selector
content=driver.find_element_by_css_selector('body ul a#rank')
print(content)
# %%
content.text
# %% 네이버 뉴스
# https://news.naver.com
# 검색 : //*[@id="lnb.searchForm"]/fieldset/input[1]
# 버튼 : //*[@id="lnb.searchForm"]/fieldset/button/span

url='https://news.naver.com'
driver.get(url)

search_xpath=driver.find_element_by_xpath('//*[@id="lnb.searchForm"]/fieldset/input[1]')
btn_xpath=driver.find_element_by_xpath('//*[@id="lnb.searchForm"]/fieldset/button/span')

print(search_xpath)
print(btn_xpath)
# %%

search_xpath.send_keys('미세먼지')
btn_xpath.click()

# %% 실습 2
# 네이버 또는 다음에서 검색하고 버튼 누르기 해보기

# %%
url='https://naver.com'
driver.get(url)

bar_xpath=driver.find_element_by_xpath('//*[@id="query"]')
button=driver.find_element_by_xpath('//*[@id="search_btn"]')

bar_xpath.send_keys('블소')
button.click()
# %%
