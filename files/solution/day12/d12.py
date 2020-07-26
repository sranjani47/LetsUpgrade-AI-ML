#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
dataset=pd.read_csv('general_data_attr_change.csv')
dataset.head()


# In[11]:


dataset.columns


# In[12]:


from scipy.stats import pearsonr
dataset['TotalWorkingYears']=dataset['TotalWorkingYears'].fillna(11.28)
dataset.columns


# In[13]:


dataset


# In[14]:


stats, p=pearsonr(dataset.attr_in_int, dataset.Age)
print(stats, p)


# As r = -0.159, there’s low negative correlation between Attrition and Age
# As the P value of 1.996 is > 0.05, we are accepting H0 and hence there’s no significant correlation
# between Attrition & Age
# 

# In[15]:


stats, p=pearsonr(dataset.attr_in_int, dataset.DistanceFromHome)
print(stats, p)


# As r = -0.009, there’s low negative correlation between Attrition and DistanceFromHome
# As the P value of 0.518 is > 0.05, we are accepting H0 and hence there’s no significant correlation
# between Attrition & DistanceFromHome
# 

# In[16]:


stats, p=pearsonr(dataset.attr_in_int, dataset.Education)
print(stats, p)


# As r = -0.015, there’s low negative correlation between Attrition and Education
# As the P value of 0.315 is > 0.05, we are accepting H0 and hence there’s no significant correlation
# between Attrition & Education
# 

# In[17]:


stats, p=pearsonr(dataset.attr_in_int, dataset.MonthlyIncome)
print(stats, p)


# As r = -0.031, there’s low negative correlation between Attrition and MonthlyIncome
# As the P value of 0.038 is < 0.05, we are accepting Ha and hence there’s significant correlation
# between Attrition & MonthlyIncome
