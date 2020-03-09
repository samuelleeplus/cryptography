#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
from lfsr import *

length = 100
##########################
print ("LFSR: **************")
L = 5
C = [0]*(L+1)
S = [0]*L

C[0] = C[2] = C[5] = 1 # 1+x^2+x^5


for i in range(0,L):            # for random initial state
    S[i] = random.randint(0, 1)
print ("Initial state: ", S) 

keystream = [0]*length
for i in range(0,length):
     keystream[i] = LFSR(C, S)
    
print ("First period: ", FindPeriod(keystream))
print ("L and C(x): ", BM(keystream))
print ("keystream: ", keystream)


# In[10]:


if (pow(2,5)-1)== FindPeriod(keystream):
    print("It is the maximum period.")
else:
    print("It is not the maximum period.")
        


# In[12]:


# 1+x^2+x^3+x^5

C2= [0]*(L+1)

C2[0] = C2[2] = C2[3] = C2[5] = 1

keystream = [0]*length
for i in range(0,length):
     keystream[i] = LFSR(C2, S)
    
print ("First period: ", FindPeriod(keystream))
print ("L and C(x): ", BM(keystream))
print ("keystream: ", keystream)


# In[13]:



if (pow(2,5)-1)== FindPeriod(keystream):
    print("It is the maximum period.")
else:
    print("It is not the maximum period.")

