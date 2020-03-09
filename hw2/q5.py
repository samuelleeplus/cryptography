#!/usr/bin/env python
# coding: utf-8

# In[21]:


import random
from lfsr import *

keystream = [1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0]
    
print ("First period: ", FindPeriod(keystream))
print ("L and C(x): ", BM(keystream))


# In[22]:


k2 = [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print ("First period: ", FindPeriod(k2))
print ("L and C(x): ", BM(k2))


# In[23]:


k3 = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
print ("First period: ", FindPeriod(k3))
print ("L and C(x): ", BM(k3))


# In[28]:


def BMA(sequence):
    N = len(sequence)
    s = sequence[:]

    for k in range(N):
        if s[k] == 1:
            break
    f = set([k + 1, 0])  # use a set to denote polynomial
    l = k + 1

    g = set([0])
    a = k
    b = 0

    for n in range(k + 1, N):
        d = 0
        for ele in f:
            d ^= s[ele + n - l]

        if d == 0:
            b += 1
        else:
            if 2 * l > n:
                f ^= set([a - b + ele for ele in g])
                b += 1
            else:
                temp = f.copy()
                f = set([b - a + ele for ele in f]) ^ g
                l = n + 1 - l
                g = temp
                a = b
                b = n - l + 1

    # output the polynomial
    def print_poly(polynomial):
        result = ''
        lis = sorted(polynomial, reverse=True)
        for i in lis:
            if i == 0:
                result += '1'
            else:
                result += 'x^%s' % str(i)

            if i != lis[-1]:
                result += ' + '

        return result

    return (print_poly(f))


# In[30]:


print("The degree polynomial is: ",BMA(k2))

