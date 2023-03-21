"""1. For this challenge, you are supposed to find the sum of the digits of a two-digit number.
45 ➞ 9
38 ➞ 11
67 ➞ 13
"""


x = 45
y = x // 10 + x %10
print(y)


x = int(45)

y = x % 10

x = x // 10

z = x % 10

print(y + z)



x = int(38)

y = x % 10

x = x // 10

z = x % 10

print(y + z)


x = int(67)

y = x % 10

x = x // 10

z = x % 10

print(y + z)
