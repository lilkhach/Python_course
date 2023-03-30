"""1. Create a function that takes a string and returns it as an integer.

Examples
"6" ➞ 6

"1000" ➞ 1000

Notes
All numbers will be whole.
All numbers will be positive."""



# x = "1000"

# print(int(x))




"""2. Create a function that takes a boolean variable flag and returns it as a string.

Examples

True ➞ "True"

False ➞ "False" """


# Value = bool(False)


# print(str(Value))




"""3. Write a function that returns the string "something" joined with a space " " and the given argument a.

Examples
"is better than nothing" ➞ "something is better than nothing"

"Bob Jane" ➞ "something Bob Jane"

"something" ➞ "something something" """


# a = "is better than nothing"

# print("something", a)



"""4. Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

Person	Relation
Darth Vader	father
Leia	sister
Han	brother in law
R2D2	droid

Examples
"Darth Vader" ➞ "Luke, I am your father."

"Leia" ➞ "Luke, I am your sister."

"Han" ➞ "Luke, I am your brother in law." """


# name = input("Please, enter the name >")

# x = "Luke, I am your " 
# y = "father"
# a = "sister"
# b = "brother in low"
# c = "droid"

# print(((x + y) * (name == "Darth Vader")) + ((x + a) * (name == "Leia")) + ((x + b) * (name == "Han")) + ((x + c) * (name == "R2D2")))





"""5. Create a function that takes a string and returns the number (count) of vowels contained within it.

Examples
"Celebration" ➞ 5

"Palm" ➞ 1

"Prediction" ➞ 4
Notes
a, e, i, o, u are considered vowels (not y).

EXTRA Knowledge"""



# vowels = list('aeiou')
# s = input("insert the text: ").lower()
# num_vow = sum([s.count(i) for i in vowels])
 
# print(num_vow)




# consonants = 'bcdfgjklmnpqrstvxzhwy'

# vow_txt = exclude("Celebration", "bcdfgjklmnpqrstvxzhwy")

# print(len(vow_txt))



"""6. Create a function that returns True if a given inequality expression is correct and False otherwise.

Examples
"3 < 7 < 11" ➞ True

"13 > 44 > 33 > 1" ➞ False

"1 < 2 < 6 < 9 > 3" ➞ True"""


# ineq = "1 < 2 < 6 < 9 > 3"

# print(eval(ineq))




"""7. Create a function that replaces all the vowels in a string with a specified character.

Examples
"the aardvark", "#" ➞ "th# ##rdv#rk"

"minnie mouse", "?" ➞ "m?nn?? m??s?"

"shakespeare", "*" ➞ "sh*k*sp**r*" """


vowels = "a, e, i, o, u"

string = "the aardvark"

x = string.replace("a", "#") + string.replace("e", "#")

print(x)



"""8. Write a function that takes a credit card number and only displays the last four characters. 
The rest of the card number must be replaced by ************.

Examples
"1234123456785678" ➞ "************5678"

"8754456321113213" ➞ "************3213"

"35123413355523" ➞ "**********5523" """




# cc_number = input("please, insert the credit card number ->")


# print(cc_number[-4:].rjust(len(cc_number), '*'))



"""9. Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.

Examples
"Donald Trump" ➞ "Trump Donald"

"Rosie O'Donnell" ➞ "O'Donnell Rosie"

"Seymour Butts" ➞ "Butts Seymour" """

# name = "Seymour Butts"

# print(' '.join(reversed(name.split(' '))))


"""10. An isogram is a word that has no duplicate letters. 
Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".

Examples
"Algorism" ➞ True

"PasSword" ➞ False
# Not case sensitive.

"Consecutive" ➞ False
"""


# txt = "Consecutive" 
# txt = txt.lower()

# print((txt.isalpha()) and len(txt) == len(set(txt)))



"""11. Create a function to test if a string is a valid pin or not. 
A valid pin has:
- Exactly 4 or 6 characters,
- Only numerical characters (0-9),
- No whitespace

Examples:
valid("1234") ➞ True
valid("45135") ➞ False
valid("89abc1") ➞ False
valid("900876") ➞ True
valid(" 4983") ➞ False

Notes - Empty strings should return False when tested"""


# pin = "1234"

# print((len(pin) == 4 or len(pin) == 6) and (pin.isnumeric()) and (not pin.isspace()))

