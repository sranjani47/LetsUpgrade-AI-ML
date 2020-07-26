#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
dataset=pd.read_csv('general_data_updated.csv')
dataset.head()


# In[2]:


dataset.columns


# In[3]:


from scipy.stats import mannwhitneyu
a1=dataset.dis_yes
a2=dataset.dis_no
stat, p=mannwhitneyu(a1,a2)
print(stat, p)


# As the P value of 0.0 is < 0.05, the H0 is rejected and Ha is accepted.
# H0: There is no significant differences in the Distance From Home between attrition (Y) and attirition
# (N)
# Ha: There is significant differences in the Distance From Home between attrition (Y) and attirition (N)

# In[4]:


from scipy.stats import mannwhitneyu
a1=dataset.edu_yes
a2=dataset.edu_no
stat, p=mannwhitneyu(a1,a2)
print(stat, p)


# As the P value of 0.0 is < 0.05, the H0 is rejected and Ha is accepted.
# H0: There is no significant differences in the Education between attrition (Y) and attirition
# (N)
# Ha: There is significant differences in the Education between attrition (Y) and attirition (N)

# In[5]:


from scipy.stats import mannwhitneyu
a1=dataset.mon_yes
a2=dataset.mon_no
stat, p=mannwhitneyu(a1,a2)
print(stat, p)


# As the P value is again 0.0, which is < than 0.05, the H0 is rejected and ha is accepted.
# H0: There is no significant differences in the income between attrition (Y) and attirition (N)
# Ha: There is significant differences in the income between attrition (Y) and attirition (N)
