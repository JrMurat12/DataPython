#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import statsmodels.api as sm


# In[6]:


dados = pd.read_csv("mtcars.csv")
dados


# In[7]:


dados.describe()


# In[9]:


X = dados ['wt']
y = dados ['mpg']
X = sm.add_constant (X)
model = sm.OLS(y, X).fit()
model.summary()


# In[10]:


X = dados ['hp']
y = dados ['mpg']
X = sm.add_constant (X)
model = sm.OLS(y, X).fit()
model.summary()


# In[12]:


X = dados [['hp', 'wt']]
y = dados ['mpg']
X = sm.add_constant (X)
model = sm.OLS(y, X).fit()
model.summary()


# In[13]:


dados.corr()


# In[15]:


X = dados[['hp', 'wt', 'cyl']]
y = dados ['mpg']

X = sm.add_constant (X)
model = sm.OLS(y, X).fit()
model.summary()


# In[17]:


X = dados[['wt', 'cyl', 'disp']]
y = dados ['mpg']

X = sm.add_constant (X)
model = sm.OLS(y, X).fit()
model.summary()


# In[18]:


X = dados[['wt', 'cyl', 'hp']]
y = dados ['mpg']

X = sm.add_constant (X)
model = sm.OLS(y, X).fit()
model.summary()


# In[ ]:




