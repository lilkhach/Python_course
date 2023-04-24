"""1. Using .sort() method, create a lambda function that sorts the list in descending order. Refrain from using the reverse parameter.


(Hint: lambda will be passed to sort method's key parameter as argument)


Please check out Hint 0 below to be informed about a glitch regarding this exercise.


lst=[100, 10, 10000, 1, 9, 999, 99]"""

def desc(lst: list):
    lst.sort(key=lambda i: -i)
    return lst

print(desc([100, 10, 10000, 1, 9, 999, 99]))





"""2. Using sorted() function, reverse parameter and lambda sort the tuples in the list based on the last character of the second items in reverse order.

lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
#Type your answer here."""

lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]

sorted_lst = sorted(lst, key=lambda x: x[1][-1], reverse=True)
print(sorted_lst)


"""Decorators, function inside function
3. Write function which take a function as an input and run it and print how count how many times I have run the input provide functions."""
