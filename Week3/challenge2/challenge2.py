"""1. Emmy has written a function that returns a greeting to users. 
However, she's in love with Mubashir, and would like to greet him slightly differently. 
She added a special case in her function, but she made a mistake.

Can you help her?

Examples
"Matt" ➞ "Hello, Matt!"

"Helen" ➞ "Hello, Helen!"

"Mubashir" ➞ "Hello, my Love!"""


# name = input ("Enter the name, please >")

# greeting = ("Hello" + str(name)) + (name == "Mubashir") * "Hello, my Love!"

# print(greeting)


# name = input("Enter the name, please >")

# y = "Hello, " + name + "!"
# x = "Hello, my Love!"

# print(x * (name == "Mubashir") + y * (name != "Mubashir"))

# name = (liza+koma*x) + (koma)


"""2. Create a function that takes two arguments. 
Both arguments are integers, a and b. Return True if one of them is 10 or if their sum is 10.

Examples
a,b = 9, 10 ➞ True

a,b = 9, 9 ➞ False

a,b = 1, 9 ➞ True """


# a = 9
# b = 10

# print((a and b == 10) or (a + b == 10))


"""3. Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.

Examples
5 ➞ True

-55 ➞ True

37 ➞ False """

# x = 5

# print(x % 5 == 0)


"""4. Extra Knowledge 
Create a function that takes two strings as arguments and return either 
True or False depending on whether the total number of characters in the first string is equal to the total number 
of characters in the second string.

Examples
"AB", "CD" ➞ True

"ABC", "DE" ➞ False

"hello", "edabit" ➞ False"""

# str1 = "ABC"
# str2 = "CD"

# print(len(str1) == len(str2))


"""5. Given a string, return True if its length is even or False if the length is odd."""

# string = "moon"

# len("sun")

# print(len(string) % 2 == 0)


"""6. Create a function that takes a string txt and a number n and returns the repeated string n number of times.

If given argument txt is not a string, return Not A String !!

Examples
"Mubashir", 2 ➞ "MubashirMubashir"

"Matt", 3 ➞ "MattMattMatt"

1990, 7 ➞ "Not A String !!"
"""

# txt = 1990
# n = 3
# print((txt * n) or (txt != True, str * "Not A String!"))

text, repeat = 1990, 3
tramabanakan = type(text) == str
print(text * repeat * tramabanakan or "Not A String!!" * (not tramabanakan))
