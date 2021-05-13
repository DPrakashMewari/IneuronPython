#!/usr/bin/env python
# coding: utf-8

# In[21]:


"""
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

"""
import operator
from operator import itempgetter

l1 = []
while True:
    user_details = input()
    if not user_details:
        break
    l1.append(tuple(user_details.split(" ")))
print(sorted(l1, key=itemgetter(0,1,2)))
        




# In[59]:


# Define a class with a generator which can iterate the numbers, which are divisible by 7, 
#between a given range 0 and n.

n = 100
for i in range(0,n):
    i = i+1
    if i % 7 == 0:
        print(i)


# In[61]:


# 
def iterateit(n):
    i = 0 
    while i<n:
        j = i
        i = i +1
        if j % 7 == 0:
            yield j
x2 = [x1 for x1 in iterateit(100)]
print(x2)

