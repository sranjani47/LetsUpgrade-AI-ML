#!/usr/bin/env python
# coding: utf-8
Q1. Subtraction of Complex number
# In[1]:


cn1 = complex(input("Enter first complex number - "))
cn2 = complex(input("Enter second complex number - "))
cn = cn1 - cn2
print('The subtraction of given complex number is',cn)

Q2. 4th Root
# In[2]:


n = int(input("Enter the number to find 4th square root: "))
print("solution type 1", n**0.25)   
print("solution type 2", n**(1/4))
import math
print("solution type 3", math.sqrt(math.sqrt(n)))

Q3. Swapping two Numbers using temporary variable
# In[3]:


a = int(input("Enter first number a - "))
b = int(input("Enter second number b - "))
print("Before swapping a =",a," b =",b)
c = a
a = b
b = c
print("After swapping a =",a," b =",b)

Q4. Swapping two Numbers without temporary variable
# In[4]:


a = int(input("Enter first number a - "))
b = int(input("Enter second number b - "))
print("Before swapping a =",a," b =",b)
a = a + b
b = a - b
a = a - b
print("After swapping a =",a," b =",b)

Q5. Calculating kelvin and celcius from Fahrenheit
# In[5]:


F = int(input("Enter temperature to be converted into kelvin and celcius - "))
print("Temperature in Kelvin ( K ) = {:.3f}".format(273.5 + ((F - 32.0) * (5.0/9.0))))
print("Temperature in Celcius ( C ) = {:.3f}".format((F - 32) * 5 / 9))

Q6. Demonstration of variable data types
# In[6]:


x_str = "Hello World"
print(type(x_str))
x_int = 20
print(type(x_int))
x_float = 20.5
print(type(x_float))
x_complex = 1j
print(type(x_complex))
x_list = ["apple", "banana", "cherry"]
print(type(x_list))
x_tuple = ("apple", "banana", "cherry")
print(type(x_tuple))
x_dict = {"name" : "John", "age" : 36}
print(type(x_dict))
x_set = {"apple", "banana", "cherry"}
print(type(x_set))
x_boolean = True
print(type(x_boolean))

