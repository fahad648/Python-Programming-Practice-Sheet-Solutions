#!/usr/bin/env python
# coding: utf-8

# # QUESTION 3.17:

# In[1]:


#A
def eval(x):
    i=(2*3)+1
    return i
eval(1)


# In[3]:


#B
def eval(x):
    i='Hello!!'
    return i
eval('Hello')


# In[9]:


#C
def eval(x):
    i=print('Hello'+' '+'World!!')
    return i
eval(1)


# In[11]:


#D
def eval(x):
    i="'ASCII'.count('I')"
    return i
eval(2)


# In[14]:


#E
def eval(g):
    i='x+5'
    return i
eval(5)
    


# # QUESTION 3.18:

# In[15]:


#A
a,b,c=3,4,5
if a<b:
    print('OK')


# In[18]:


#B
a,b,c=3,4,5
if c<b:
    print('OK')
else:
    print('Condition is false')


# In[19]:


#C
a,b,c=3,4,5
if a+b==c:
    print('OK')
else:
    print('Condition is false')


# In[21]:


#D
a,b,c=3,4,5
if a**2+b**2==c**2:
    print('OK')
else:
    print('Conndition is false')


# # QUESTION 3.19:

# In[22]:


#A
a,b,c=3,4,5
if a<b:
    print('OK')
else:
    print('NOT OK')


# In[23]:


#B
a,b,c=3,4,5
if c<b:
    print('OK')
else:
    print('NOT OK')


# In[24]:


#C
a,b,c=3,4,5
if a+b==c:
    print('OK')
else:
    print('NOT OK')


# In[25]:


#D
a,b,c=3,4,5
if a**2+b**2==c**2:
    print('OK')
else:
    print('NOT OK')


# # QUESTION 3.20:

# In[3]:


lst=['january','febuary','march']
for i in lst:
    print(i[:3])


# # QUESTION 3.21:

# In[26]:


lst=[2,3,4,5,6,7,8,9]
i=0
for i in lst:
    if i%2==0:
        print(i)
    


# # QUESTION 3.22:

# In[4]:


lst=[2,3,4,5,6,7,8,9]
for i in lst:
    if i**2%8==0:
        print(i)
    


# # QUESTION 3.23:

# In[26]:


i-0
for i in range(2):
    print(i)


# # QUESTION 3.24:

# In[94]:


def list(*words):
    for i in words:
        s='secret'
        if i!=s:
            print(i) 
list('cia','secret','mi6','secret')


# # QUESTION 3.25:

# In[42]:


def f(*x):
    for i in x:
        if i[0] in 'AaMm':
            print(i)
f('fahad','anum','afreen','muhib')


# # QUESTON 3.26:

# In[80]:


def f(*x):
    print('The first elements is : ',x[0])
    print('The last element is : ',x[3])
f(1,2,3,4)


# # QUESTION 3.27:

# In[77]:


def multiple(x):
    n_1=x*1
    n_2=x*2
    n_3=x*3
    n_4=x*4
    print(n_1,n_2,n_3,n_4,end=' ')
multiple(5)


# # QUESTION 3.28:

# In[90]:


i=0
def square(*num):
    for i in num:
        i=i-1
        i**2
        print(i)
square(3)
        


# # QUESTION 3.29:

# In[ ]:


i=0
def divisor(num):
    i=1
    while i<=num:
        if (num%i==0):
            i=i+1
            print(i)
            
divisor(49)
    


# # QUESTION 3.30:

# In[2]:


def average(a,b,c,d):
    print('The first number is ',a)
    print('The second number is ',b)
    print('The third number is ',c)
    print('The last number is ',d)
    if (a+b+c)/3==d:
        print('Equal!!')
    else:
        print('Not equal!!')
average(4.5,3,3,3.5)
    


# # QUESTION 3.31:

# In[4]:


def dart(x,y):
    print('Enter x : ',x)
    print('Enter y : ',y)
    r=8
    if x and y<r:
        print('It is in!!')
    else: print('You missed!!')
dart(2.5,4)


# # QUESTION 3.32:

# In[14]:


def number(a,b,c,d):
    print('enter n : ',a,b,c,d)
    print(a)
    print(b)
    print(c)
    print(d)
number(1,2,3,4)


# # QUESTION 3.33:

# In[23]:


def reverse_string(word):
    x=word[::-1]
    print(x)
reverse_string('dna')


# # QUESTION 3.34:

# In[16]:


def pay(x,y):
    vage=x*y
    if y>35:
        a=vage+125
        return a
    print(vage)
pay(10,35)
pay(10,45)
         


# # QUESTION 3.35:

# In[25]:


def prob(n):
    x=2**-n
    print(x)
prob(1)
prob(2)


# # QUESTION 3.36:

# In[57]:


def reverse_int(num):
    x=num//1.20
    print(x)
reverse_int(908)
    


# # QUESTION 3.37:

# In[70]:


from math import sqrt
def points(x1,y1,x2,y2):
    if x1==x2 and y1==y2:
        print('The slope is infinity and distnace is',d)
    m=(y2-y1)/(x2-x1)
    d=sqrt((x2-x1)+(y2-y1))
    print('The slope of line is',m,'and distnace is',d)
points(0,0,1,1)

 


# # QUESTION 3.38:

# In[73]:


def abbrevation(n):
    print(n[:2])
abbrevation('Tuesday')
abbrevation('Wednesday')
    


# # QUESTION 3.39:

# In[76]:


def collision(x1,y1,r1,x2,y2,r2):
    if x1==x2 or y1==y2:
        print('True')
    else:
        print('False')
collision(0,0,3,0,5,3)
collision(0,0,1.4,2,2,1.4)


# # QUESTION 3.40:

# In[80]:


def partition(*names):
    for i in names:
        if i[0] in 'AamM':
            print(i)
partition('Muhib','Fahad','amna','Sajid')


# # QUESTION 3.41:

# In[84]:


def lastF(first_name,last_name):
    print(last_name,(first_name[:1]),'.')
lastF('Albert','Camus')


# # QUESTION 3.42:

# In[89]:


def avg(a,b,c,d,e,f):
    average_1=(a+b+c+d)/4
    average_2=(e+f)/2
    print(average_1)
    print(average_2)
avg(95,92,86,87,66,54)


# # QUESTION 3.43:

# In[90]:


def hit(a,b,c,d,e):
    if d>c or e>c:
        print('False')
    else:
        print('True')
hit(0,0,3,3,0)
hit(0,0,3,4,0)


# # QUESTION 3.44:

# In[ ]:


def distance(x):
    

