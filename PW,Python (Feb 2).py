#!/usr/bin/env python
# coding: utf-8

# In[6]:



#Q1. **Explain with an example when to use a for loop and a while loop:**

#For loop:** Use a for loop when you know the number of iterations you need. For example, when iterating over elements of a list, characters of a string, or a range of numbers.
# Example of for loop
for i in range(5):
    print(i)

#While loop:** Use a while loop when you're unsure about the number of iterations you need, but you have a condition that must be satisfied for the loop to continue.
# Example of while loop
i = 0
while i < 5:
    print(i,end=" ")
    i += 1
    


# In[7]:


#Q2. **Write a Python program to print the sum and product of the first 10 natural numbers using for and while loop:**

# Using for loop
sum_for = 0
product_for = 1
for i in range(1, 11):
    sum_for += i
    product_for *= i
print("Sum using for loop:", sum_for)
print("Product using for loop:", product_for)

# Using while loop
sum_while = 0
product_while = 1
i = 1
while i <= 10:
    sum_while += i
    product_while *= i
    i += 1
print("Sum using while loop:", sum_while)
print("Product using while loop:", product_while)



# In[8]:


#Q3. **Create a Python program to compute the electricity bill for a household:**

units = int(input("Enter units of electricity consumed: "))
bill = 0
if units <= 100:
    bill = units * 4.5
elif units <= 200:
    bill = 100 * 4.5 + (units - 100) * 6
elif units <= 300:
    bill = 100 * 4.5 + 100 * 6 + (units - 200) * 10
else:
    bill = 100 * 4.5 + 100 * 6 + 100 * 10 + (units - 300) * 20
print("Electricity bill: Rs.", bill)


# In[9]:


#Q4. **Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print that list:**


# Using for loop
cube_list_for = []
for num in range(1, 101):
    cube = num ** 3
    if cube % 4 == 0 or cube % 5 == 0:
        cube_list_for.append(num)
print("Cube list using for loop:", cube_list_for)

# Using while loop
cube_list_while = []
num = 1
while num <= 100:
    cube = num ** 3
    if cube % 4 == 0 or cube % 5 == 0:
        cube_list_while.append(num)
    num += 1
print("Cube list using while loop:", cube_list_while)



# In[10]:


#Q5. **Write a program to filter count vowels in the given string:**


string = "I want to become a data scientist"
vowels = 'aeiouAEIOU'
vowel_count = sum(1 for char in string if char in vowels)
print("Count of vowels:", vowel_count)

