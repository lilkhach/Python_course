"""1. Given a list, rotate the values clockwise by one (the last value is sent to the first position).

Check the examples for a better understanding.

Examples
[1, 2, 3, 4, 5] ➞ [5, 1, 2, 3, 4]

[6, 5, 8, 9, 7] ➞ [7, 6, 5, 8, 9]

[20, 15, 26, 8, 4] ➞ [4, 20, 15, 26, 8] """


# x = [20, 15, 26, 8, 4]

# print(x[-1:] + x[:-1])


"""2. Create a function that inverts the rgb values of a given tuple.

Examples
color_invert((255, 255, 255)) ➞ (0, 0, 0)
# (255, 255, 255) is the color white.
# The opposite is (0, 0, 0), which is black.

color_invert((0, 0, 0)) ➞ (255, 255, 255)

color_invert((165, 170, 221)) ➞ (90, 85, 34)
Notes
Must return a tuple.
255 is the max value of a single color channel. """




"""3. Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the list, return -1.

Examples
find_bob(["Jimmy", "Layla", "Bob"]) ➞ 2

find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0

find_bob(["Jimmy", "Layla", "James"]) ➞ -1
Notes
Assume all names start with a capital letter and are lowercase thereafter (i.e. don't worry about finding "BOB" or "bob"). """

names = (["Jimmy", "Layla", "Bob"])


print(names.index("Bob")) #+ ((names.index("Bob") is False) * "-1"))


"""EXTRA Knowledge
4. Given a list of numbers, write a function that returns a list that...

Has all duplicate elements removed.
Is sorted from least to greatest value.
Examples
unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]

unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]

unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7] """

# x = [6, 7, 3, 2, 1]

# print(list(set(x)))


"""EXTRA Knowledge
5. Given two strings, create a function that returns the total number of unique characters from the combined string.

Examples
count_unique("apple", "play") ➞ 5
# "appleplay" has 5 unique characters:
# "a", "e", "l", "p", "y"

"sore", "zebra" ➞ 7

"a", "soup" ➞ 5 """



# x, y = "sore", "zebra"

# print(len(set(x + y)))



"""6. Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.

Examples
{
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
} ➞ ["Becky", "John", "Steve"]"""

# x = {
#   "Student 1" : "Ashot",
#   "Student 2" : "Becky",
#   "Student 3" : "John"
# }

# print(x.values())

"""7. Create a function that returns a list of strings sorted by length in ascending order.

Examples
sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]

sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]

sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]

sort_by_length([]) ➞ []
Notes
Strings will have unique lengths, so don't worry about comparing two strings with identical length.
Return an empty array if the input array is empty """



# x = ["may", "april", "september", "august"]

# print(sorted(x, key=len))



"""8. Write a function that converts a dictionary into a list of keys-values tuples.

Examples
dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}) ➞ [("B", 2), ("C", 3), ("D", 1)]

dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)] """

# x = {
#   "likes": 2,
#   "dislikes": 3,
#   "followers": 10
# }

# y = list(x.items())
# print(y[-2:] + y[:-2])   # because the output values are rotated clockwise 


"""9. Print the value of key ‘history’ from the below dict
sample

Dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
"""


# Dict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }


# print(Dict["class"]["student"]["marks"]["history"])

"""10. Rename key of a dictionary
Write a program to rename a key city to a location in the following dictionary.

Given:

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
Expected output:

{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
"""

# x = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# x ["location"] = x.pop("city")
# print(x)