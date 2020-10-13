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

#%% 심심하니까 하는거

import time
url_bs='http://g.bns.plaync.com/ingame/bs/character/profile?c='
char_name=input('캐릭터명 : ')
page_bs=urlopen(str(url_bs)+str(char_name))
soup_bs=BeautifulSoup(page_bs, 'html.parser')

time.sleep(1)
atk=soup_bs.find('span', id='total-int_attack_power_value').text
boss_atk=soup_bs.find('span', id='total-boss_attack_power_value').text
acc=soup_bs.find('span', id='total-int_attack_hit_value').text
acc_rate=soup_bs.find('span', id='total-attack_hit_rate').text
crt_rate=soup_bs.find('span', id='total-attack_critical_rate').text
crt_dam=soup_bs.find('span', id='total-attack_critical_damage_value').text
attr=soup_bs.find('span', id='total-attack_attribute_value').text

print('공격력 :', atk)
print('항마공 :', boss_atk)
print('명중 :', acc)
print('명중률 :', acc_rate)
print('치명타율 :', crt_rate)
print('치명피해 :', crt_dam)
print('공력 :', attr)
print('치피공합 :', int(crt_dam)+int(attr))