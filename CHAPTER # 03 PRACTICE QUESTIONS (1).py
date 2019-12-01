#!/usr/bin/env python
# coding: utf-8

# # PRACTICE PROBLEM 3.1:

# In[1]:


f=eval(input("Enter the tempertaure in farenheit : "))
c=5/9*(f-32)
print(c)


# # PRACTICE PROBLEM 3.2:

# In[3]:


#A
age=eval(input('Enter your age : '))
if age>62:
    print('You can get your pansion benefits!!')
else:
    print('you are not eligible')


# In[6]:


#B
name=eval(input('Enter your name : '))
lst=['Musial','Aaraon','Williams','Gehrig','Ruth']
if name in lst:
    print('One of the top 5 baseball playes ever!!')


# In[3]:


#C
s=0
h=10 
while s<h:
    print(s,'Is less than hits')
    s=s+1
else:
    print("YOU ARE DEAD!!")


# In[6]:


#D
direction=eval(input("Enter the direction : "))
d=["north","south","east","west"]
if direction in d:
    print('YOU CAN ESCAPE!!')
else:
    print('YOU CANT..')


# # PRACTICE QUESTION 3.4:

# In[3]:


name=eval(input("enter your name:"))
n=["joe","sue","hani","sophie"]
if name in n:
    print(name,"you're login")
else:
    print("user unknown")
print("done")


# # PRACTICE QUESTION 3.3:

# In[1]:


#A
year=eval(input("Enter the year:"))
if year%4==0:
    print("could be a leap year")
else:
    print("Definately not a leap year")


# In[3]:


#B
ticket=eval(input("enter your ticket:"))
list=['1009','1003','1004','1006','1564']
if ticket in list:
    print("YOU WON!")
else:
    print("BETTER LUK NEXT TIME")


# # PRACTICE PROBLEM 3.5:

# In[9]:


list=['cat','dog','fish','frog']
for i in list:
    print(i)
    i=+1


# # PRACTICE PROBLEM 3.6:

# In[7]:


#A
for i in range(10):
    print(i)
    i=+1


# In[9]:


#B
for i in range(2):
    print(i)
    i=+1


# # PRACTICE QUESTION 3.7:

# In[11]:


#A
for i in range(3,13):
    print(i)
    i=+1


# In[17]:


#B
i=0
for i in range(0,11,2):
        print(i)
        i=+1


# In[16]:


#C
i=0
for i in range(0,24,3):
        print(i)
        i=+1


# # PRACTICE QUESTION 3.8:

# In[12]:


from math import pi
def perimeter(r):
    value=2*pi*r
    print(value)
perimeter(2)
perimeter(1)


# # PRACTICE QUESTION 3.9:

# In[17]:


def average(x,y):
    avg=(x+y)/2
    print(avg)
average(1,3)
average(2,3.5)


# # PRACTICE QUESTION 3.10:

# In[25]:


def noVowel(x):
    i=0
    for i in x:
        if i in 'aeiouAEIOU':
            print(i)
            i=+1
noVowel('SAIFULWAHABMUBEENBAIG')


# # PRACTICE QUESTION 3.11:

# In[34]:


def allEven(x):
        if i%2==0:
            print('True')
        else:
            print('False')
allEven([2,4,5,6,8,10])
allEven([2,4,6,8,10,12])


# # PRACTICE QUESTION 3.12:

# In[36]:


def negatives(x):
    for i in x:
        if i<0:
            print(i)
negatives([1,3,-3,1,-5])


# # PRACTICE QUESTION 3.14:

# In[46]:


a=[5,6,7]
b=a
a=3


# # PRACTICE QUESTION 3.15:

# In[47]:


team=['Ava','Eleanor','Clare','Sarah']
team[0]='Sarah'
team[3]='Ava'
team


# # PRACTICE QUESTION 3.16:

# In[55]:


def ingre(x):
    ingre[0]='apples'
    ingre[3]='flour'
ingre(['flour','sugar','butter','apples'])
    


# In[ ]:




