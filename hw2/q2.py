#!/usr/bin/env python
# coding: utf-8

# In[16]:


p =  5527064775949971276700546474393760569152256071781455112554572252477078482817219303694924773296938028736900310336193124455858291501008953781025760084204617
q =  10263715010889663011237581846368625560721472564413404816414563312121711111200512062338133630430698017953660509772503749526855821347556114413740814256720609
n= p*q
c= 6016447327565519594114000681088119027251827426178525282923410539353402986195693266732998286093991346837854685945523958512316911535914428131590560765331415513592957120361162167163223354643895818554169459592360948153053758601978139504376688619229954806515113869761029037549195053798048200751500102605855423415
e = 67

#Compute m = cd  mod n  (where d = e-1 mod (n)).  


# In[17]:


einv = modinv(e, n)
print(einv)


# In[18]:


import random
 
def is_Prime(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True  

is_Prime(p)


# In[29]:


is_Prime(q)


# In[30]:


eulTot = (p-1)*(q-1)
d = modinv(67,eulTot)


# In[31]:


print(d)


# In[34]:


print(pow(c,d,n))

