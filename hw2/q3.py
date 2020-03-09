#!/usr/bin/env python
# coding: utf-8

# In[95]:


#question 3
#part a
n = 333837116253674643166082492900 
a = 57063337401967433471889139534
b = 397555361861029295385484594412  


# In[96]:


from myntl import *
import math
import random
import pyprimes
import warnings

d = (gcd(a,n))
print(d)


# In[97]:


if (b%d == 0):
    print("It is divisible")


# In[98]:


mod = modinv(a//d, n//d)


# In[99]:


xVal = (mod*(b//d)) % (n//d)


# In[100]:


while d != 0:
    print("One solution to the problem is: ", xVal + ((d-1)*(n//d)))
    d = d - 1


# In[47]:


#part b
n2 = 333837116253674643166082492900
a2 = 176622984297114106732586191098 
b2 = 84172329859897226978948124629  


# In[48]:


d2 =gcd(a2,n2)


# In[60]:


if (b2%d2 == 0):
    print("It is divisible")
else:
    print("It is not divisible, and therefore there are no solutions")


# In[30]:


#part c
n3 = 333837116253674643166082492900 
a3= 320736651991764172584335713727 
b3 = 30472957776104045808802882504  


# In[67]:


print("The gcd is: ",gcd(a3,n3))


# In[64]:


d3 = modinv(a3, n3)
print("The inverse of the function is: ",d3)


# In[66]:


ans3 = (b3 * d3) % n3
print("The unique solution is: ",ans3)

