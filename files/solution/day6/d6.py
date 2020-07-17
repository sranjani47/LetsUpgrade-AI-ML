#!/usr/bin/env python
# coding: utf-8
Q1. Assuming that we have some email addresses in the "username@companyname.com" format, please write program
to print the company name of a given email address. Both user names and company names are composed of letters
only.
Input Format:
The first line of the input contains an email address.
Output Format:
Print the company name in single line.
Example;
Input:
john@google.com
Output:
google
# In[1]:


email = input("Enter the input:")
domain = (email.split('@')[1]).split('.')[0]
print(domain)

Q2. Write a program that accepts a comma-separated sequence of words as input and prints the words in a comma
separated sequence after sorting them alphabetically.
Input Format:
The first line of input contains words separated by the comma.
Output Format:
Print the sorted words separated by the comma.
Example:
Input:
without,hello,bag,world
Output:
bag,hello,without,world
# In[2]:


inputVal = input("Enter the input:")
res = ','.join(sorted(inputVal.split(',')))
print(res)

Q3. Create your own Jupyter Notebook for Sets.
Reference link: https://www.w3schools.com/python/python_sets.asp


Set:
A set is a collection which is unordered and unindexed, using {}
# In[3]:


myset = {"tom", "jerry", "duck"}
print(myset)
for x in myset:
  print(x)
'''If want to check value present or not in set'''
print("\nIf want to check value present or not in set\n")
print("jerry" in myset)
print("jerry1" in myset)

'''Add Item to set'''
print("\nAdd Item to set\n")
myset.add("dora")
print(myset)

'''add multiple values to set'''
print("\nadd multiple values\n")
myset.update(["rio", "angrybird", "sonic"])
print(myset)

print("\nGet length of set \n")
print(len(myset))

print("\nRemove value from set -- > rio\n")
myset.remove("rio")
print(myset)

''' pop() => Sets are unordered, so when using the pop() method, you will not know which item that gets removed.'''
print("\npop() => Sets are unordered, so when using the pop() method, you will not know which item that gets removed.\n")
myset.pop()
print(myset)

Q4. Given a list of n-1 numbers ranging from 1 to n, your task is to find the missing number. There are no duplicates.
Input Format:
The first line contains n-1 numbers with each number separated by a space.
Output Format:
Print the missing number
Example:
Input:1 2 4 6 3 7 8
Output:5
Explanation:
In the above list of numbers 5 is missing and hence 5 is the input
# In[4]:



def removeDup(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if int(num) not in final_list: 
            final_list.append(int(num)) 
    return final_list 

def getMissingNo(inputNumbers): 
    inputNumbersLst = removeDup(inputNumbers.split(" "))
    print(inputNumbersLst)
    n = len(inputNumbersLst) 
    total = (n + 1)*(n + 2)/2
    sumOfNumbers = sum(inputNumbersLst)
    return total - sumOfNumbers 

inputNumbers = input("Enter the list of numbers - ")
missedNo = getMissingNo(inputNumbers) 
print(missedNo) 

Q5. With a given list L, write a program to print this list L after removing all duplicate values with original order reserved.
Example:
If the input list is
12 24 35 24 88 120 155 88 120 155
Then the output should be
12 24 35 88 120 155
# In[5]:


def getOrderNo(inputNumbers): 
    inputNumbersLst = removeDup(inputNumbers.split(" "))
    return sorted(inputNumbersLst)

inputNumbers = input("Enter the list of numbers - ")
orderedNo = getOrderNo(inputNumbers)
print(' '.join(map(str,orderedNo))) 

