#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset1=pd.read_csv("general_data.csv")
dataset1.head()


# In[4]:


dataset1.columns


# In[5]:


dataset1


# In[6]:


dataset1.isnull()


# In[7]:


dataset1.duplicated()


# In[8]:


dataset1.drop_duplicates()


# In[9]:


dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome',
'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear',
'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].describe()
dataset3


# In[10]:


dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome',
'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear',
'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].median()
dataset3


# In[11]:


dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome',
'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear',
'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].mode()
dataset3


# In[12]:


dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome',
'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear',
'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].var()
dataset3


# In[13]:


dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome',
'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear',
'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].skew()
dataset3


# In[14]:


dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome',
'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear',
'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].kurt()
dataset3


# Inference from the analysis:
# 
# All the above variables show positive skewness; while Age & Mean_distance_from_home are leptokurtic and all other variables are platykurtic.
# The Mean_Monthly_Income’s IQR is at 54K suggesting company wide attrition across all income bands
# Mean age forms a near normal distribution with 13 years of IQR

# Outliers:
# There’s no regression found while plotting Age, MonthlyIncome, TotalWorkingYears,earsAtCompany, etc., on a scatter plot
# 

# In[3]:


box_plot=dataset1.Age
plt.boxplot(box_plot)


# In[4]:


box_plot=dataset1.MonthlyIncome
plt.boxplot(box_plot)


# In[5]:


box_plot=dataset1.YearsAtCompany
plt.boxplot(box_plot)


# In[ ]:




