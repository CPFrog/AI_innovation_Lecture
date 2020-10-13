#%% 실습 1 : 코스피지수(거래량, 거래대금, 장중최고, 장중최저)

url_n='https://finance.naver.com/sise/sise_index.nhn?code=KOSPI'
page_n=urlopen(url_n)
soup_n=BeautifulSoup(page_n, 'html.parser')

quant=soup_n.find('td',id='quant').text
amount=soup_n.find('td',id='amount').text
high=soup_n.find('td',id='high_value').text
low=soup_n.find('td',id='low_value').text
print(quant, amount, high, low)

#%% 심화 1 : 52주 최고, 52주 최저 불러오기

max_52=soup_n.find_all('td',class_='td')[2].text
min_52=soup_n.find_all('td',class_='td2')[2].text
print(max_52, min_52)

#%% JS의 blind로 가린 정보 스크럼

url_samasung='https://finance.naver.com/item/main.nhn?code=005930'
page_samsung=urlopen(url_samasung)
soup_s=BeautifulSoup(page_samsung, 'html.parser')
div_now=soup_s.find('div', class_='today')
now=div_now.find('span',class_='blind').text
print(now)