"""1.	Write a map function that adds plus 5 to each item in the list."""


def plus_five(x):
        return x + 5

rand_list = [1, 3, 4, 8, 10]
    
print(list(map(plus_five, rand_list)))


"""2.	Write a map function that adds "Hello, " in front of each item in the list."""


def greet(a):
        return f"Hello, {a}"

new_list = [1, 4, "a", 12.5]

print(list(map(greet, new_list)))


"""3.	Using filter() function filter the list so that only negative numbers are left."""


x = [7, 6, -15, 9, -28, -5]

print(list(filter(lambda a: a < 0, x)))


"""4.	Using filter function, filter the even numbers so that only odd numbers are passed to the new list."""



x = [7, 6, -15, 9, -28, -5]

print(list(filter(lambda a: a % 2 != 0, x)))


"""5.	Using map() and filter() functions add 2000 to the values below 8000."""


num_list = [7000, 12, 9000, 845, 11548, 642, 52, 5000]

filtered_list = list(filter(lambda x: x < 8000, num_list))

print(list(map(lambda x: x + 2000, filtered_list)))


"""6.	Return product of integer lists"""

from functools import reduce

def multiply(a, b):
    return a * b

integer_list = [2, 3, 4, 5]

print(reduce(multiply, integer_list))






