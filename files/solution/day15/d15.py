#!/usr/bin/env python
# coding: utf-8

# # 1. Create a 3x3x3 array with random values 

# In[1]:


import numpy as np
x = np.random.random((3,3,3))
print(x)


# # 2.Create a 5x5 matrix with values 1,2,3,4 just below the diagonal

# In[2]:


x = np.diag([1, 2, 3, 4,5])
print(x)


# # 3.Create a 8x8 matrix and fill it with a checkerboard pattern

# In[3]:


x = np.ones((3,3))
print("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)


# # 4. Normalize a 5x5 random matrix

# In[4]:


x= np.random.random((3,3))
print("Original Array:")
print(x)
xmax, xmin = x.max(), x.min()
x = (x - xmin)/(xmax - xmin)
print("After normalization:")
print(x)


# # 5.  How to find common values between two arrays?

# In[5]:


a1 = np.array([0, 10, 20, 40, 60])
print("Array1: ",a1)
a2 = [10, 30, 40]
print("Array2: ",a2)
print("Common values between two arrays:")
print(np.intersect1d(a1, a2))


# # 6.How to get the dates of yesterday, today and tomorrow?

# In[6]:


yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print("Yestraday: ",yesterday)
today     = np.datetime64('today', 'D')
print("Today: ",today)
tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow: ",tomorrow)


# # 7. Consider two random array A and B, check if they are equal

# In[7]:


x = np.random.randint(0,2,6)
print("First array:")
print(x)
y = np.random.randint(0,2,6)
print("Second array:")
print(y)
print("Test above two arrays are equal or not!")
array_equal = np.allclose(x, y)
print(array_equal)


# # 8.Create random vector of size 10 and replace the maximum value by 0 

# In[8]:


x = np.random.random(10)
print("Original array:")
print(x)
x[x.argmax()] = 0
print("Maximum value replaced by 0:")
print(x)


# # 9. How to print all the values of an array?

# In[9]:


x = np.zeros((4, 4))
print(x)


# # 10.Subtract the mean of each row of a matrix

# In[10]:


print("Original matrix:\n")
X = np.random.rand(2, 4)
print(X)
print("\nSubtract the mean of each row of the said matrix:\n")
Y = X - X.mean(axis=1, keepdims=True)
print(Y)


# # 11.Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? 

# In[ ]:


print("Original matrix:\n")
X = np.random.rand(2, 4)
print(X)
print("\nAdding 1 :\n")
Y = X.mean(axis=1, keepdims=True) + 1
print(Y)


# In[ ]:





# # 12.How to get the diagonal of a dot product?

# In[ ]:





# # 13.How to find the most frequent value in an array?

# In[11]:


x = np.random.randint(0, 10, 40)
print("Original array:")
print(x)
print("Most frequent value in the above array:")
print(np.bincount(x).argmax())


# # 14.How to get the n largest values of an array

# In[12]:


x = np.arange(10)
print("Original array:")
print(x)
np.random.shuffle(x)
n = 1
print (x[np.argsort(x)[-n:]])


# # 15.How to create a record array from a regular array?

# In[13]:


arra1 = np.array([("aaa", 88.5, 90),
                 ("bbb", 87, 99),
             ("ccc", 85.5, 91)])
print("Original arrays:")
print(arra1)
print("\nRecord array;")
result = np.core.records.fromarrays(arra1.T,
                              names='col1, col2, col3',
                              formats = 'S80, f8, i8')
print(result)


# In[ ]:




