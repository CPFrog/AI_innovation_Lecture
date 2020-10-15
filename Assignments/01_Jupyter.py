#!/usr/bin/env python
# coding: utf-8

# ### 문제 1.
# * 현재 기온을 입력받아, if문을 이용하여
#     * 27도 이상이면 반바지를 입으세요.
#     * 27도 미만이면 긴바지를 입으세요. 출력하기

# In[1]:


temp=input("현재 기온을 입력하세요 : ")
temp=int(temp)

if temp>=27 : 
    print("반바지를 입으세요.")
else : 
    print("긴바지를 입으세요.")


# ### 문제 2.
#  * 정수를 입력받아,
#   * 입력된 값이 짝수이면 짝수라고 출력
#   * 입력된 값이 홀수이면 홀수라고 출력
#  * (Hint) % 연산자 이용해보기

# In[2]:


num=input("정수를 입력하세요 : ")
num=int(num)

if(num%2==0):
    print("짝수")
else : 
    print("홀수")


# ### 문제 3.
#  * 성적을 입력받아,
#   * 95점 이상이면 그랜드 마스터
#   * 90점 이상이면 커널 마스터
#   * 80점 이상이면 익스퍼트
#   * 70점 이상이면 초심자
#   * 나머지는 해당하지 않음 출력하기
#  * (Hint) elif 이용하기

# In[3]:


score = input("점수를 입력하세요 : ")
score = int(score)

if score>=95 :
    print("그랜드 마스터")
elif score>=90 :
    print("커널 마스터")
elif score>=80 :
    print("익스퍼트")
elif score>=70 :
    print("초심자")
else : 
    print("해당하지 않음")


# ### 문제 4.
#  * for를 이용하여 10부터 20까지 정수합을 구하는 프로그램 만들기

# In[5]:


sum=0

for i in range (10,21) :
    sum+=i

print(sum)


# ### 문제 5.
#  * 하나의 문자(string)를 입력받아, 숫자를 제거하는 프로그램을 만들어보자.

# In[23]:


s=input("여기에 입력하세요 : ")
ans=''

for x in s:
    if x>='0' and x<='9' :
        continue
    else :
        ans+=x

print(ans)


# ### 문제 6.
#  * 가위바위보 를 하나 입력받아, 컴퓨터와 내가 누가 이겼는지 비겼는지 출력하는 프로그램 만들기
#  * 컴퓨터의 값은 임의로 여러분이 입력해도 된다. 랜덤 함수를 이용해도 된다.

# In[16]:


import random
select=input("선택(가위,바위,보) : ")
if select=='가위':
    select=1
elif select=='바위':
    select=2
elif select=='보':
    select=3

com_select=random.randrange(1,4)
com=''
if com_select==1:
    com='가위'
elif com_select==2:
    com='바위'
else :
    com='보'

print("컴퓨터의 선택 :", com)

if com_select==3:
    if select==1:
        print("유저가 이겼습니다.")
    elif select==com_select:
        print("비겼습니다.")
    else :
        print("컴퓨터가 이겼습니다.")
else:
    if select>com_select:
        print("유저가 이겼습니다.")
    elif select==com_select:
        print("비겼습니다.")
    else :
        print("컴퓨터가 이겼습니다.")


# ### 문제 7.
#  * 0~10 사이의 값을 입력받아,
#  * 컴퓨터가 생각한 숫자를 3회 안에 맞추는 프로그램 만들어보기
#  * 맞추면 맞췄다고 이야기하기

# In[5]:


import random

com=random.randrange(0,11)

for i in range(1,4):
    x=input("숫자를 입력하세요(0~10) : ")
    x=int(x)
    if(x==com):
        print("OOO 맞췄습니다! OOO")
    elif x!=com and i<3:
        print("XXX 틀렸습니다. 다시 시도해보세요. XXX \n")
    else :
        print("XXX 틀렸습니다. 다음 기회에 맞춰보세요. XXX \n")


# ### 번외.
#  * 문제 7번을 응용하여 0~100까지의 정수로 up-down 게임을 만들어라.
#  * 사용자에게 주어지는 기회는 최대 5회이다.
#  * 사용자가 입력한 숫자와 컴퓨터의 숫자가 다를 경우, 출력문을 통해 큰지 작은지 여부를 알려주어야 한다.

# In[9]:


import random

com=random.randrange(0,101)

for i in range(0,5):
    x=input("숫자를 입력하세요(0~100) : ")
    x=int(x)
    if(x==com):
        print("OOO 맞췄습니다! OOO")
    elif x>com and i<4:
        print("▽▽▽ 틀렸습니다. 더 작은 수에요. ▽▽▽ \n")
    elif x<com and i<4:
        print("△△△ 틀렸습니다. 더 큰 수에요. △△△ \n")
    else :
        print("5번의 기회 모두 틀렸습니다.")
        print("정답은", com ,"입니다.")


# In[ ]:




