"""EXTRA Knowledge
1. Given three lists of integers: lst1, lst2, lst3, return the sum of integers which are common in all three lists.

Examples
sum_common([1, 2, 3], [5, 3, 2], [7, 3, 2]) ➞ 5
// 2 & 3 are common in all 3 lists.

sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]) ➞ 7
// 2, 2 & 3 are common in all 3 lists.

sum_common([1], [1], [2]) ➞ 0 """

# lst1, lst2, lst3 = [1, 2, 3], [5, 3, 2], [7, 3, 2]

# st1, st2, st3 = set(lst1), set(lst2), set(lst3)

# stw = st1 & st2 & st3

# x = stw.intersection()

# print(sum(x))   #anyway, this solution doesn't work for example 2(((





"""EXTRA Knowledge
2. Write a function that takes a list of numbers and returns a list with two elements:

The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.
Example
[1, 2, 3, 4, 5, 6] ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

[-1, -2, -3, -4, -5, -6] ➞ [-12, -9]

[0, 0] ➞ [0, 0]
Notes
Count 0 as an even number. """


# num = [1, 2, 3, 4, 5, 6]

# sum_odd = sum([x for x in num if x % 2 != 0])
# sum_even = sum([x for x in num if x % 2 == 0])


# print([sum_even, sum_odd])


"""3. Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects 
like { "name": "John", "top_note": 5 }.

Examples
top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }

top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }

top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 } """


# x = { "name": "Max", "notes": [1, 4, 6] }

# highest_note = sorted(x["notes"], reverse=True)[0]

# print({"name": x["name"], "top_note": highest_note})


"""EXTRA Knowledge
4. Write a function that takes a list of numbers and returns a list with two elements:

The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.
Example
sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])

sum_odd_and_even([0, 0]) ➞ [0, 0]) """


#this is the same 2nd challenge




"""5. You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. 
You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory. 
Return the total profit made, rounded to the nearest dollar.

Examples
profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}) ➞ 14796

profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}) ➞ 32411

profit({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
}) ➞ 44030 """


# data = {
#   "cost_price": 225.89,
#   "sell_price": 550.00,
#   "inventory": 100
# }

# profit = round((data['sell_price'] - data['cost_price']) * data['inventory'])

# print(profit)



"""6. A number is said to be Harshad if it's exactly divisible by the sum of its digits. 
Create a function that determines whether a number is a Harshad or not.

Examples
is_harshad(75) ➞ False
# 7 + 5 = 12
# 75 is not exactly divisible by 12
 
is_harshad(171) ➞ True
# 1 + 7 + 1 = 9
# 9 exactly divides 171
 
is_harshad(481) ➞ True

is_harshad(89) ➞ False

is_harshad(516) ➞ True

is_harshad(200) ➞ True """


# num = 89

# x = (num // 100) + (num % 100) // 10 + num % 10

# print(num % x == 0)


"""EXTRA Knowledge
7. Given an input string, reverse the string word by word.

Examples
"the sky is blue" ➞ "blue is sky the"

"  hello world!  " ➞ "world! hello"

"a good  example" ➞ "example good a"
Notes
A word is defined as a sequence of non-space characters.
The input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
Try to solve this in linear time. """



# string = "the sky is blue"

# lst = string.split()

# lst.reverse()

# rstring = " ".join(lst)

# print(rstring)




"""Extra Knowledge
8. Create a function that builds a word from the scrambled letters contained in the first list. 
Use the second list to establish each position of the letters in the first list. 
Return a string from the unscrambled letters (that made-up the word).

Examples
word_builder(["g", "e", "o"], [1, 0, 2]) ➞ "ego"

word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]) ➞ "test"

word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2]) ➞ "edabit" """


# lst1, lst2 = ["g", "e", "o"], [1, 0, 2]

# st1 = "".join(lst1)
# st2 = ", ".join(str(i) for i in lst2)


# print(st1[st2])
# print(st2)






"""9. Create a function to test if a string is a valid pin or not.

A valid pin has:

Exactly 4 or 6 characters.
Only numerical characters (0-9).
No whitespace.
Examples
valid("1234") ➞ True

valid("45135") ➞ False

valid("89abc1") ➞ False

valid("900876") ➞ True

valid(" 4983") ➞ False
Notes 
Empty strings should return False when tested. """


# pin = " 4983"

# print((len(pin) == 4 or len(pin) == 6) and (pin.isnumeric()) and (not pin.isspace()))


"""10. Return a new set of identical items from two sets

Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:

{40, 50, 30} """

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}


# print(set1.intersection(set2))


"""11. Write a Python program to return a new set with unique items from both sets by removing duplicates.

Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:

{70, 40, 10, 50, 20, 60, 30} """


# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# print(set1.union(set2))


"""12. Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.

Given:

set1 = {10, 20, 30}
set2 = {20, 40, 50}
Expected output:

set1 {10, 30} """

# set1 = {10, 20, 30}
# set2 = {20, 40, 50}

# set1.difference_update(set2)

# print(set1)

"""EXTRA Knowledge
13. Given an input string, reverse the string word by word (reversed word also).

Examples
"the sky is blue" ➞ "eulb si yks eht"

Notes
A word is defined as a sequence of non-space characters.
The input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
Try to solve this in linear time.
"""


# str1 = "the sky is blue"


# str2 = str1[::-1]

# lst = str2.split()

# str3 = " ".join(lst)


# print(str3)