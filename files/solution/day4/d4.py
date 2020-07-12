#!/usr/bin/env python
# coding: utf-8
Q1. Research on whether addition, subtraction, multiplication, division, floor division and modulo
operations be performed on complex numbers. Based on your study, implement a Python
program to demonstrate these operations.

Addition, subtraction, multiplication, division will support 
Floor division and modulo doesn't support - Complex numbers are numbers with a real and imaginary part. 
They're only worth noting here because neither modulo nor floor division can accept a complex number as an operand. 
Trying to use a complex number for floor division or modulo operations will raise a TypeError.
# In[4]:


''''''
cn1 = complex(input("Enter first complex number - "))
cn2 = complex(input("Enter second complex number - "))
add = cn1 * cn2
sub = cn1 - cn2
mul = cn1 * cn2
div = cn1 / cn2
print('Addition:', add)
print('Subtraction', sub)
print('Multiplication', mul)
print('Division', div)

Q2. Research on range() functions and its parameters. Create a markdown cell and write in your own
words (no copy-paste from google please) what you understand about it. Implement a small
program of your choice on the same.


range() is used to create sequence of numbers, It has 3 parameters. parameters are start, stop and step
start - It specifying which position to start and its default value is 0
stop - It specifying which postion to stop, that position always be (stop number - 1)
step - It specifying the incrementation

# In[7]:


for x in range(6):
  print('start example:',x)
for x in range(3, 6):
  print('stop example:',x)
for x in range(3, 8,2):
  print('step example:',x)

Q3. Consider two numbers. Perform their subtraction and if the result of subtraction is greater than
25, print their multiplication result else print their division result.
# In[9]:


n1 = int(input("Enter first number - "))
n2 = int(input("Enter second number - "))

sub = n1 - n2
if sub > 25:
    print("Result", n1 * n2)
else:
    print("REsult", n1 / n2)    

Q4. Consider a list of 10 elements of integer values. If the number in the list is divisible by 2, print the
result as "square of that number minus 2".
# In[7]:


l = [1,2,3,4,5,6,7,8,9,10]
for i in range(0, len(l)): 
    if l[i]% 2 == 0:
        print('square of that number minus 2')
        break
            

Q5. Consider a list of 10 elements. Print all the elements in the list which are greater than 7 when that
number is divided 2.
# In[8]:


l = [1,2,3,4,5,6,7,8,9,10]
for i in range(0, len(l)): 
    if l[i]% 2 == 0 and l[i] > 7:
        print(l[i])

