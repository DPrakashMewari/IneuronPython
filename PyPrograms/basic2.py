#!/usr/bin/env python
# coding: utf-8

# In[10]:


"""
Write a program to generate and print another tuple whose 
values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
"""


tp1 = (1,2,3,4,5,6,7,8,9,10)
l1 = []
for i in tp1:
    if i%2 == 0:
        l1.append(i)
tuple(l1)


# In[11]:


"""
Write a program which accepts a string as input to print "Yes" 
if the string is "yes" or "YES" or "Yes", otherwise print "No". 
"""

input1 = input("")
if input1 == "YES" or "Yes" or "yes":
    print("Yes")
else:
    print("No")


# In[16]:


"""
Write a program which can filter even numbers in a list by using filter function.
The list is: [1,2,3,4,5,6,7,8,9,10].

"""

l1  = [1,2,3,4,5,6,7,8,9,10]


x1=filter(lambda x: x%2==0,l1)
for i in x1:
    print(i)


# In[32]:


"""
Python Program to Print the Fibonacci number

"""

def fibonnaci(n):
    a = 0
    b = 1
    if n <= 0:
        print("Please try again")
    elif n == 0:
        return 0
    elif n == 1:
        return b 
    else:
        for i in range(1,n):
            c = a + b
            a = b 
            b = c 
        return b 

    
fibonnaci(n = int(input()))


# In[37]:


"""
Python Program to Print the Fibonacci Sequence ?

"""


def fibonnacisequence(n):
    a = 0 
    b = 1 
    if n <= 0:
        return "Please try again"
    elif n == 1:
        return b 
    elif n == 0:
        return a 
    else:
        for i in range(n-1):
            c = a + b
            a = b 
            b = c 
            print(c)
        


# In[40]:


"""
Define a class named Rectangle which can be constructed by a length and width.
The Rectangle class has a method which can compute the area. 

"""

class Rectangle:
    def __init__(self,l,w):
        self.l = l 
        self.w = w 
    def area(self):
        area = self.l * self.w
        return area
obj = Rectangle(2,10)
obj.area()

