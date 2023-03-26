"""1. Create a function that takes a list containing only numbers and return the first element.

Examples
[1, 2, 3] ➞ 1

[80, 5, 100] ➞ 80

[-500, 0, 50] ➞ -500"""

#solution 1

# x = [80, 5, 100]

# print(x[0])



#solution 2

# x = [80, 5, 100]

# print(x[-3])


"""2.  Create a function that takes a list of numbers. Return the largest number in the list.

Examples
[4, 5, 1, 3] ➞ 5

[300, 200, 600, 150] ➞ 600

[1000, 1001, 857, 1] ➞ 1001"""


# x = [1000, 1001, 857, 1]

# print(max(x))


"""3. Create a function that takes a list of numbers and returns the smallest number in the list.

Examples
[34, 15, 88, 2] ➞ 2

[34, -345, -1, 100] ➞ -345

[-76, 1.345, 1, 0] ➞ -76

[0.4356, 0.8795, 0.5435, -0.9999] ➞ -0.9999

[7, 7, 7] ➞ 7"""


# x = [34, -345, -1, 100]

# print(min(x))


"""4. Create a function that takes a list and returns the difference between the biggest and smallest numbers.

Examples

[10, 4, 1, 4, -10, -50, 32, 21] ➞ 82
# Smallest number is -50, biggest is 32.

[44, 32, 86, 19] ➞ 67
# Smallest number is 19, biggest is 86."""

# x = [44, 32, 86, 19]

# print(max(x) - min(x))


"""5. Create a function to concatenate two integer lists.

Examples
[1, 3, 5], [2, 6, 8] ➞ [1, 3, 5, 2, 6, 8]

[7, 8], [10, 9, 1, 1, 2] ➞ [7, 8, 10, 9, 1, 1, 2]

[4, 5, 1], [3, 3, 3, 3, 3] ➞ [4, 5, 1, 3, 3, 3, 3, 3]"""

#solution 1

# list1 = [7, 8]
# list2 = [10, 9, 1, 1, 2]

# list1.extend(list2)

# print(list1)



#solution 2

# list1 = [7, 8]
# list2 = [10, 9, 1, 1, 2]

# print([*list1, *list2])


"""6. Given a list of numbers, return True if the sum of the values in the list is less than 100; otherwise return False.

Examples
[5, 57] ➞ True

[77, 30] ➞ False

[0] ➞ True"""


# x = [77, 30]

# print(sum(x) < 100)




"""7. Given a list of integers, determine whether the sum of its elements is even or odd.

The return value should be a string "odd" or "even".

If the input list is empty, consider it as a list with a zero [0].

Examples
[0] ➞ "even"

[1] ➞ "odd"

[] ➞ "even"

[0, 1, 5] ➞ "even" """


# x = [0, 1, 5]

# print("even" * (sum(x) % 2  == 0) + "odd" * (sum(x) % 2))





"""8. Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

Examples
"11/12/2019" ➞ "20191211"

"12/31/2019" ➞ "20193112"

"01/15/2019" ➞ "20191501" 
EXTRA Knowledge"""


date = "12/31/2019"

fdate = date.replace("/", " ")
rdate = fdate.split()
rdate.reverse()

print(''.join(rdate))


# import datetime

# d = datetime.datetime.strptime("11/12/2019", "%d/%m/%Y")
# fd = d.strftime('%Y%m%d')

# print(fd)


"""9. Create a function that takes two numbers as arguments num, length and returns a list of multiples of num until the list length reaches length.

Examples
7, 5 ➞ [7, 14, 21, 28, 35]

12, 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

17, 6 ➞ [17, 34, 51, 68, 85, 102]"""


# number, lenght  = 12, 10

# print(list(range(number, number*lenght+1, number)))


"""10. Create a function that takes a list of numbers lst, a string s and return a list of numbers as per the following rules:

"Asc" returns a sorted list in ascending order.
"Des" returns a sorted list in descending order.
"None" returns a list without any modification.
Examples
[4, 3, 2, 1], "Asc"  ➞ [1, 2, 3, 4]

[7, 8, 11, 66], "Des" ➞ [66, 11, 8, 7]

[1, 2, 3, 4], "None" ➞ [1, 2, 3, 4]

"""

# list = [7, 8, 11, 66]

# function = input("Plese, insert the function >")

# Asc = sorted(list)
# Des = sorted(list, reverse = True)
# Non = list

# print((Asc * (function == "Asc")) or (Des * (function == "Des")) or (Non * (function == "None")))