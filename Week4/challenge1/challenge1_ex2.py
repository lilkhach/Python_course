"""2. A repdigit is a positive number composed out of the same digit. 
Create a function that takes an two-digit integer and returns whether it's a repdigit or not.
44 ➞ True
45 ➞ False
-44 ➞ False
"""

x = 44
y = x //10
z = x % 10
print(y == z)


x = 44

# print(x % 44 == 0)


x = 45

#print(x % 44 == 0)


x = - 44

#print(x % 44 == 0)