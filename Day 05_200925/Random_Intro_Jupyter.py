#!/usr/bin/env python
# coding: utf-8

# In[1]:


def two_minus(a,b):
    return a-b

print(two_minus(2,5))


# In[2]:


str1="Hello World!"

list1=[1,2,3,4]

tuple=(1,2,3,4)

dic={"a":["apple", "animal"] , "b":['banana', 'boat']}


# In[5]:


s1="Hello World!"

print(s1[0])
print(s1[1])
print(s1[-1])
print(s1[-5:-2])


# ## 2-3 
# * 첫번째 값 선택
# * 두번쨰 값 선택
# *[3,4,5] 선택

# In[7]:


list=[1,2,3,4,5]

print(list[-5])
print(list[1])
print(list[2:5])


# In[8]:


for i in range(0,10,1):
    print(i)


# ### 3-2 홀수만 출력

# In[12]:


for i in range(1,10,2) : 
    print(i)


# In[13]:


spring = ['봄', '여름', '가을', '겨울']
for one in spring:
    print(one)


# ### 3-3 좋아하는 과일 출력

# In[14]:


fruit=['메론','수박','블루베리']
for i in fruit :
    print(i)


# In[16]:


fruit=['메론','수박','블루베리']

inp = input("좋아하는 과일은? : ")
for i in fruit :
    if i==inp :  
        print("그 과일 있어")


# In[21]:


s=input("문자열 입력 : ")
str1='aeiouAEIOU'

result=""

for i in s : 
    print(i, end=' ')
    if i not in str1 :  
        result = result+i

print('\n')
print("result:", result)


# In[5]:


import random

all_str=""
for x in range(97,123):
    all_str+=chr(x)
print(all_str)

def passGen():
    password=""
    
    # 8글자 암호
    for i in range(8):
        idx=random.randrange(len(all_str))
        password+=all_str[idx]
    return password
    
passGen()


# ### 대문자로 임의의 암호 10자리 생성

# In[9]:


import random
def passGen():
    password=""
    
    for i in range(10):
        idx=random.randrange(len(all_str))
        password+=all_str[idx].upper()
    return password
passGen()


# In[ ]:




