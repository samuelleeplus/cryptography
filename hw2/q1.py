#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
import random
import fractions

gcdList = []

for i in range(1,61):
    if math.gcd(i,61) == 1:
        gcdList.append(i)
        
print(len(gcdList))


# In[13]:


import sys
import random
def generator(p):
    l=[]
    for x in range (1,p):
        rand = x
        exp=1
        nex = rand % p

        while (nex != 1 ):
            nex = (nex*rand) % p
            exp = exp+1
        if (exp==p-1):
            l.append(rand)
            
    return l


# In[15]:


print(generator(61))


# In[20]:


#Find a subgroup of Z_61^*, whose order is 5. Find also its generator.
import argparse


def calculate_subgroups(modulus):
    def get_group(coprime):
        return tuple(sorted(generate_subgroup(coprime, modulus)))

    return {get_group(coprime) for coprime in get_coprimes(modulus)}

def generate_subgroup(factor, modulus, start=1):
    while True:
        yield start
        start = (start * factor) % modulus

        if start == 1:
            return

def get_coprimes(number):
    return (i for i in range(1, number) if gcd(number, i) == 1)


# In[21]:


print(calculate_subgroups(61))


# In[22]:


print("The subgroup with order 5 is: 1, 9, 20, 34, 58")


# In[ ]:




