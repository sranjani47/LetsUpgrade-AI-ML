#!/usr/bin/env python
# coding: utf-8
Q1. Write a Python program to find the first 20 non-even prime natural numbers.
# In[1]:


def check_prime(input_number):
    if input_number > 1:
        for i in range(2, input_number):
            if (input_number % i) == 0:
                res = "No"
                break
        else:
            res = "Yes"
    else:
        res = "No"        
    return res

listVar = []
v = ""
lst1 = list(range(3,100,2))
for i in lst1:
    if len(listVar) < 20:
        v = check_prime(i)
        if(v == "Yes"):
            listVar.append(i)
print(listVar)

Q2. Write a Python program to implement 15 functions of string
# In[2]:


strVal = "Lets Upgrade"
print(strVal.capitalize())
print(strVal.casefold())
print(strVal.isalnum())
print(strVal.count("e"))
print(strVal.index("p"))
print(strVal.encode())
print(strVal.isalpha())
print(strVal.isdigit())
print(strVal.isspace())
print(strVal.islower())
print(strVal.split(" "))
print(strVal.replace("g","h"))
print(strVal.swapcase())
print(strVal.lower())
print(strVal.isupper())

Q3. Write a Python program to check if the given string is a Palindrome or Anagram or None of them.
Display the message accordingly to the user.
# In[4]:


str1 = str(input("Enter the word - "))
str2 = str(input("Enter the second word - "))
if(str1 == str1[::-1] ):
    print("Its palindrome")
elif(sorted(str1)== sorted(str2)): 
    print("Its anagrams.") 
else:
    print("None of them")

Q4. Write a Python's user defined function that removes all the additional characters from the string
and converts it finally to lower case using built-in lower(). eg: If the string is "Dr. Darshan Ingle
@AI-ML Trainer", then the output be "drdarshaningleaimltrainer"
# In[5]:


str1 = str(input("Enter the word - "))
resultVal = ""
for character in str1:
    if character.isalnum():
        resultVal += character.lower()
print(resultVal)

