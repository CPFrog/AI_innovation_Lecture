#!/usr/bin/env python
# coding: utf-8

# ### 문제 1 - input, float()
#  * '나' 는 통계학과 재학중이다.
#  * 학점은 140학점을 이수해야 하며, 평점은 2.5이상이 되어야 졸업이 가능하다.
#  * if문과 A and B 연산자를 이용하여 졸업이 가능한지, 졸업이 안되는지 확인해 보자.
#   * 학점과 평점을 입력받는다.
#   * 140이상, 2.5이상 졸업
#   * 그외 조건 졸업이 힙듭니다.
#   * 학점과 평점은 정수가 아니므로 float( input() )의 형태로 입력받아야 한다.

# In[1]:


credit = float(input("이수한 학점을 입력하세요 : "))
avg = float(input("평점을 입력해 주세요 : "))

if credit>=140 and avg>=2.5 : 
#if credit<140 or avg<2.5 : 
    print("졸업이 힘듭니다.")
else : 
    print("졸업 가능합니다.")


# ### 문제 2 - 클래스
# * 아래 계산기 클래스에 곱하기 기능을 추가하시오.

# In[4]:


class CalFnc2 :
    def __init__(self, result):
        self.result = result

    def plus (self, num):
        self.result += num
        return self.result

    def sub (self, num):
        self.result -= num
        return self.result
# --------------------------------------     
    def mul (self, num):
        self.result *= num
        return self.result


# In[5]:


a = CalFnc2(0)  # 계산기 한대

## 첫 초기값(result)
print(a.result)

## 더하기 기능
print(a.plus(5))

#곱하기 기능
print(a.mul(4))


# ### 문제 3 - while문을 이용하여 로그인
# * while문을 이용하여 5번까지만 id가 있는지 확인하는 프로그램을 작성하시오.
#  * 초기의 id는 사용자가 정한다.
#  * 매번 id를 입력받는다.
#  * 있으면 있어요. 없으면 id가 없어요. 매번 출력한다.
#  * id가 있는지 확인이 되면 break를 이용하여 벗어난다.

# In[6]:


ori_id = 'toto'

num=0
while num != 5 :
    input_id = input("ID를 입력해주세요 : ")
    if ori_id==input_id : 
        print("ID가 있습니다.")
        break;
    else : 
        num += 1
        print("ID가 없습니다.")


# ### 문제 4
# * 세 개의 단어를 입력 받아, 맨 마지막줄에 '각각의 단어의 뒤에서 두번째 알파벳'을 연결하여 출력하는 프로그램을 작성하시오.

# In[1]:


word1 = input("첫번째 단어를 입력해 주세요. ")
word2 = input("두번째 단어를 입력해 주세요. ")
word3 = input("세번째 단어를 입력해 주세요. ")

ac = word1[-2] + word2[-2] + word3[-2]
print(ac)


# ### 문제 5
# * 세개의 상품과 가격을 아래와 같이 입력하여 text파일을 만들자.
# * mydata.txt
#  * 상품1, 5000
#  * 상품2, 10000
#  * 상품3, 100000
# * 파일을 불러와서 전체 내용을 출력하시오.
# * open() 함수 이용

# In[2]:


w = open('mydata.txt', 'w')
w.write('상품1. 5000\n')
w.write('상품2. 10000\n')
w.write('상품3. 1000\n')
w.close()

r = open('mydata.txt', 'r')
print(r.read())
r.close()


# ### 문제 6
# * 위의 파일에 상품 4와 가격을 입력받아 추가하는 프로그램을 작성하시오.
# * (hint) 'a' 모드 이용

# In[3]:


a = open('mydata.txt', 'a')
d=input('추가할 상품과 가격을 입력하세요 : ')
a.write(d+'\n')
a.close()

r = open('mydata.txt', 'r')
print(r.read())
r.close()


# ### 문제 7
# * 하나의 이미지를 복사하는 프로그램을 작성하시오.
#  * 복사된 이미지에 대한 파일을 올리도록 한다.

# In[11]:


import os
path_dir=os.getcwd()

f_list = os.listdir(path_dir)
f_list


# In[10]:


file1 = input("원본 파일 입력 : ")
file2 = input("복사 파일 입력 : ")

infile = open(file1, 'rb')
outfile = open(file2, 'wb')

while True :
    copy_buffer = infile.read(1024)
    if not copy_buffer:
        break
    outfile.write(copy_buffer)

infile.close()
outfile.close()
print("복사 완료")


# ### 문제 8
# * 방문하고 싶은 url 5개를 리스트로 만들고,
# * 희망하는 사이트를 선택지에서 선택하여 해당 사이트를 열어주는 프로그램을 작성하시오.
# * ex) 희망하는 웹페이지를 선택하세요.
#  * 1. 네이버　　2. 다음　　3. 구글　　4. lms　　5. 구글원격데스크톱
# * 입력은 모두 숫자로만 이뤄진다고 가정한다.

# In[27]:


import webbrowser

url_list = ['https://naver.com', 'https://daum.net', 'https://google.com', 
           'http://lms.ictcog.kr', 'https://remotedesktop.google.com/support']
url_name = ['네이버', '다음', '구글', 'lms', '구글 원격 데스크톱']

print('방문하고자 하는 웹 사이트를 선택하세요.')
print('　1. 네이버 　　2. 다음 　　3. 구글 　　4. lms 　　5. 구글 원격 데스크톱')
select=int(input("희망하는 웹사이트 : "))

webbrowser.open(url_list[select-1])


# ## 심화 문제.
# ### 아래 조건을 8번문제의 조건에 추가하여 정상적으로 실행되는 코드를 작성하시오.
# 
# * 선택지의 번호뿐 아니라 사이트명으로도 해당 웹페이지를 열 수 있도록 한다.  
# 이 때, 두가지 방식의 입력이 동시에 이뤄지지는 않는다고 가정한다.  
# 　(입력 예시) 　1　,　다음　 　// 　　(입력 불가 예시) 　1. 네이버  
#   
#   
# * 원하는 사이트가 없는 경우, 사용자가 직접 웹사이트 주소를 입력하고  
# 그 주소를 웹브라우저로 열어주는 프로그램을 작성한다.  
# (hint) 선택지 6번을 만든다면..??

# In[4]:


import webbrowser

url_list = ['https://naver.com', 'https://daum.net', 'https://google.com', 
           'http://lms.ictcog.kr', 'https://remotedesktop.google.com/support']
url_name = ['네이버', '다음', '구글', 'lms', '구글 원격 데스크톱']

print('방문하고자 하는 웹 사이트를 선택하세요.')
print('　1. 네이버 　2. 다음 　3. 구글 　4. lms 　5. 구글 원격 데스크톱 　6. 주소 직접 입력')
select=input("희망하는 웹사이트 : ")

if select>='0' and select<='9' : 
    select=int(select)
    if select>6 or select<1 : print('번호가 잘못 입력되었습니다.')
    elif select==6 : 
        url=input("희망하는 웹사이트 주소를 입력하세요 : ")
        webbrowser.open(url)
    else: 
        webbrowser.open(url_list[select-1])

else:
    for i in range(0,7) :
        if i==6 : print('해당 이름의 웹사이트는 선택지에 없습니다.')
        elif select=='주소 직접 입력' : 
            url=input("주소를 입력하세요 : ")
            webbrowser.open(url)
            break
        elif i<5 and url_name[i]==select: 
            webbrowser.open(url_list[i])
            break

