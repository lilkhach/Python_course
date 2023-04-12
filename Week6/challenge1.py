"""1. Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

Person	Relation
Darth Vader	father
Leia	sister
Han	brother in law
R2D2	droid
Examples
relation_to_luke("Darth Vader") ➞ "Luke, I am your father."

relation_to_luke("Leia") ➞ "Luke, I am your sister."

relation_to_luke("Han") ➞ "Luke, I am your brother in law." """


name = input("Enter the name, please: ")


if name == "Darth Vader":
    print("Luke, I am your father.")
elif name == "Leia":
    print("Luke, I am your sister.")
elif name == "Han":
    print("Luke, I am your brother in law.")
elif name == "R2D2":
    print("Luke, I am your droid.")
else:
    print("This person has no relation to Luke.")


"""2. Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time.

Examples
damage(40, 5, "second") ➞ 200

damage(100, 1, "minute") ➞ 6000

damage(2, 100, "hour") ➞ 720000
Notes
Return "invalid" if damage or speed is negative. """


damage = 2
speed = 100
time = "hour"


if time == "second":
    damage_amount = damage * speed
    print(damage_amount)
elif time == "minute":
    damage_amount = damage * speed * 60
    print(damage_amount)
elif time == "hour":
    damage_amount = damage * speed * 3600
    print(damage_amount)
else:
    damage < 0 or speed < 0
    print("invalid")

"""3. Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.

Examples
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]

filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]

filter_list(["Nothing", "here"]) ➞ [] """


lst = ["A", 0, "Edabit", 1729, "Python", "1729"]

print([i for i in lst if isinstance(i, int)])


"""4. Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. 
A number is symmetrical when it is the same as its reverse.

Examples
is_symmetrical(7227) ➞ True

is_symmetrical(12567) ➞ False

is_symmetrical(44444444) ➞ True

is_symmetrical(9939) ➞ False

is_symmetrical(1112111) ➞ True """


num = 1112111

stnum = str(num)

print((stnum == stnum[::-1]))


"""5. Create a function that changes all the elements in a list as follows:

Add 1 to all even integers, nothing to odd integers.
Concatenates "!" to all strings and make the first letter of the word a capital letter.
Changes all boolean values to its opposite.
Examples
change_types(["a", 12, True]) ➞ ["A!", 13, False]

change_types([13, "13", "12", "twelve"]) ➞ [13, "13!", "12!", "Twelve!"]

change_types([False, "False", "true"]) ➞ [True, "False!", "True!"]
Notes
There won't be any float values.
You won't get strings with both numbers and letters in them.
Although the task may be easy, try keeping your code as clean and as readable as possible! """

x = [13, "13", "12", "twelve", False]

return_value = []

for i in x:
    if isinstance(i, str):
        return_value.append(i.capitalize() + "!")
    elif isinstance(i, bool):
        return_value.append(not i)
    elif isinstance(i, int):
        if i%2:
            return_value.append(i)
        else:
            return_value.append(i+1)
    
    else:
        print(f"Can not parse {i}")
print(return_value)


"""6. Create a function that takes a string s and returns a list of two-paired characters. 
If the string has an odd number of characters, add an asterisk * in the final pair.

See the below examples for a better understanding:

Examples
string_pairs("mubashir") ➞ ["mu", "ba", "sh", "ir"]

string_pairs("edabit") ➞ ["ed", "ab", "it"]

string_pairs("airforces") ➞ ["ai", "rf", "or", "ce", "s*"]
Notes
Return [] if the given string is empty. """





"""7. Create a function that takes two parameters and, if both parameters are strings, 
add them as if they were integers or if the two parameters are integers, concatenate them.

Examples
stupid_addition(1, 2) ➞ "12"

stupid_addition("1", "2") ➞ 3

stupid_addition("1", 2) ➞ None
Notes
If the two parameters are different data types, return None.
All parameters will either be strings or integers. """

x = "1"
y = "2"


if isinstance(x, int) and isinstance(y, int):
    print(str(x) + str(y))
elif isinstance(x, str) and isinstance(y, str):
    if x.isdigit() and y.isdigit():
        print(int(x) + int(y))
    else:
        print(None)
else:
    print(None)



"""8. Write a function that does the following operations: adding, subtracting, dividing, or multiplying values. 
It is simply referred to as variable operation variable. 
Of course, the variables have to be defined, but in this challenge the variables will be defined for you. 
All you have to do is look at the variables, do some string to integer conversions, use some if conditionals, and combine them based on the operation.

The numbers and operation will be given as strings, and you should return the value as a string as well.

Examples
operation("1", "2", "add" ) ➞ "3"

operation("4", "5", "subtract") ➞ "-1"

operation("6", "3", "divide") ➞ "2"
Notes
The numbers and operation will be given as strings, and you should also return the value as a string.
If the answer is "undefined", return "undefined" (e.g. dividing by zero).
For divide, go ahead and round down to an integer. """


x = "6"
y = "2"
operation = "divide"


if operation == "add":
    result = str(int(x) + int(y))
    print(result)

elif operation == "subtract":
    result = str(int(x) - int(y))
    print(result)

elif operation == "multiply":
    result = str(int(x) * int(y))
    print(result)

elif operation == "divide":
    if y != 0:
        result = str(int(x) // int(y))
        print(result)
    else:
        result = "undefined"        #however, this doesn't work when y=0, and in output I got zeroDivisionError(
        print(result)
else:
    result = "undefined"
    print(result)


"""9. Check if the given string consists of only letters and spaces and if every letter is in lower case.

Examples
letters_only("PYTHON") ➞ False

letters_only("python") ➞ True

letters_only("12321313") ➞ False

letters_only("i have spaces") ➞ True

letters_only("i have numbers(1-10)") ➞ False

letters_only("") ➞ False
Notes
Empty arguments will always return False.
Input values will be mixed (symbols, letters, numbers). """

st = "python1"

if all(i.isalpha() or i.isspace() for i in st) and all(i.islower() or i.isspace() for i in st):
    print(True)

elif st == "":
    print(False)
                        # can't find the solution for empty string. Always returns True.
elif len(st) == 0:
    print(False)

else:
    print(False)


"""10. Write a function that takes a list and determines whether it's strictly increasing, strictly decreasing, or neither.

Examples
check([1, 2, 3]) ➞ "increasing"

check([3, 2, 1]) ➞ "decreasing"

check([1, 2, 1]) ➞ "neither"

check([1, 1, 2]) ➞ "neither"
Notes
The last example does NOT count as strictly increasing, since 1-indexed 1 is not strictly greater than the 0-indexed 1.
Input lists have a minimum length of 2."""


lst = [1, 3, 10, 6]

y = sorted(lst)
z = sorted(x, reverse=True)




if lst[0] < lst[1] < lst[2] < lst[3]:
    print("increasing")

elif lst[0] > lst[1] > lst[2] > lst[3]:
    print("decreasing")

else:
    print("neither")


# or 2nd solution. But two variants have disadvantages.
if len(lst) <=2 or len(set(x)) != len(lst):
elif lst == sorted(lst):
    print("increasing")

elif lst == sorted(lst, reverse=True):
    print("decreasing")

else:
    print("neither")




