#!/usr/bin/env python
# coding: utf-8

# # PROGRAMMING PA2
# 
# ## NORMALIZATION PROBLEM

# In[4]:


import numpy as np

X = np.random.random((5,5))
print(X)


# In[5]:


xmean = np.mean(x)
xstd = np.std(x)
z = (x-xmean/xstd)
print(z)


# In[6]:


np.save('X_normalized.npy' , z)


# ## DIVISIBLE BY 3 PROBLEM

# In[16]:


array = np.arange(1, 101)
x = array ** 2
d3 = x.reshape(10,10)
print(d3)


# In[17]:


div3 = x[x%3==0]
print(div3)


# In[18]:


np.save('div-by-3.np', x[x%3==0])


# In[ ]:




