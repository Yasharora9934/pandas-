#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


a=np.arange(12).reshape(3,4)
a


# In[7]:


for raw in a:
    print (raw)


# In[8]:


for raw in a:
    for cell in raw:
        print (cell)


# In[9]:


for cell in a.flatten():
        print (cell)


# In[11]:


for x in np.nditer(a,order='F'):
    print(x)


# In[14]:


for x in np.nditer(a,order='F',flags=['external_loop']):
    print(x)


# In[20]:


for x in np.nditer(a,op_flags=['readwrite']):
    x[...]=x*x


# In[21]:


a


# In[22]:


a*a


# In[23]:


a


# In[29]:


b=np.arange(3,15,4).reshape(3,1)
b


# In[26]:


a


# In[30]:


b


# In[33]:


for x,y in np.nditer([a,b]):
    print(x,y)


# In[ ]:




