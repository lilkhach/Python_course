"""1. Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a 
string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

Here, we have 1 followed by a space, operator followed by another space and 2. 
For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

Notes

    All the inputs are only integers.
    The operators are * - + and //.
    Hint: Think about the single space that appears before and after the arithmetic operator."""

def arithmetic_operation(x: str):
    y = x.split()
    n1 = int(y[0])
    n2 = int(y[2])
    oper = y[1]

    if oper == "+":
        return n1 + n2
    elif oper == "-":
        return n1 - n2
    elif oper == "*":
        return n1 * n2
    elif oper == "//":
        if n2 == 0:
            return -1
        else: 
            return n1 // n2
    else:
        return None

            

# print(arithmetic_operation("12 + 12") == 24)

# print(arithmetic_operation("12 - 12") == 0)

# print(arithmetic_operation("12 * 12") == 144)

# print(arithmetic_operation("12 // 0") == -1)




"""2. A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

Create a function that determines whether a number is a Disarium or not.
Examples

is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32

is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

is_disarium(544) ➞ False

is_disarium(518) ➞ True

is_disarium(466) ➞ False

is_disarium(8) ➞ True

Notes

    Position of the digit is 1-indexed."""



def is_disarium(x: int):
    y = str(x)
    digit_sum = sum(int(digit)**(index+1) for index, digit in enumerate(y))
    return digit_sum == x


# print(is_disarium(544) == False)

# print(is_disarium(518) == True)

# print(is_disarium(466) == False)

# print(is_disarium(8) == True)



#solution 2



def is_disarium(x: int):
    y = str(x)
    y_len  = len(y)
    
    digit_sum = sum(int(y[i])**(i+1) for i in range(y_len))
    
    return digit_sum == x




"""3. Write a function that takes a list of lists and returns the value of all of the symbols in it, 
where each symbol adds or takes something from the total score. Symbol values:

    # = 5
    O = 3
    X = 1
    ! = -1
    !! = -3
    !!! = -5

A list of lists containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.

If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and a X would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return 0.

Notes

Strings in the lists will only be #, O, X, !, !! and !!!."""


def check_score(sym: list):
    sym_dict = {"#": 5, "O": 3, "X": 1, "!": -1, "!!": -3, "!!!": -5}
    value = 0
    for sublst in sym:
        for i in sublst:
            value += sym_dict[i]
    return max(value, 0)
        

  
# print(check_score([
#   ["#", "!"],
#   ["!!", "X"]
# ]) == 2)

# print(check_score([
#   ["!!!", "O", "!"],
#   ["X", "#", "!!!"],
#   ["!!", "X", "O"]
# ]) == 0)

# print(check_score([
#   ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
#   ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
#   ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
#   ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
#   ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
#   ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
#   ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
#   ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
#   ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
#   ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
#   ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
#   ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
#   ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
#   ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
# ]) == 12)



"""4. Create a function that takes a string's characters as ASCII and returns each character's hexadecimal value as a string.
Examples

convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"

convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"

convert_to_hex("Marty Poppinson") ➞ "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"

Notes

    Each byte must be seperated by a space.
    All alpha hex characters must be lowercase."""

def convert_to_hex(string):
    hex_values = [hex(ord(char))[2:] for char in string]
    hex_string = ' '.join(hex_values)
    return hex_string


# print(convert_to_hex("hello world") == "68 65 6c 6c 6f 20 77 6f 72 6c 64")

# print(convert_to_hex("Big Boi") == "42 69 67 20 42 6f 69")

# print(convert_to_hex("Marty Poppinson") == "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e")




"""5. Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. 
Luckily, I've been able to find the vowels that were removed.

Given a censored string and a string of the censored vowels, return the original uncensored string.
Example

uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"

uncensor("abcd", "") ➞ "abcd"

uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"

Notes

    The vowels are given in the correct order.
    The number of vowels will match the number of * characters in the censored string."""


def uncensor(cen_str, vow_str):
    
    for i in vow_str:
        cen_str = cen_str.replace("*", i, 1)
    return cen_str


# print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
# print(uncensor("abcd", ""))
# print(uncensor("*PP*RC*S*", "UEAE"))





"""6. Using markdown, it's possible to format links such as https://edabit.com/challenges, into something tidier like this. 
Notice how the text "Go to the challenges!" appears when hovering over the link.

This was achieved by using this code:

[this](https://edabit.com/challenges "Go to the challenges!")

Given the url, the new name and optionally the hover_text, return the tidied up hyperlink as a string.
Examples

tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!") ➞ "[this](https://edabit.com/challenges "Go to the challenges!")"

tidy_link("https://www.google.com", "Google", "Google Search") ➞ "[Google](https://www.google.com "Google Search")"

tidy_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!") ➞ "[Click Me!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"

Notes

    Supply double quotes for the hover text.
    Keep in mind that some tests will not include an argument for hover_text."""



def tidy_link(url, name, hover=None):
    if hover:
        return f"[{name}]({url} \"{hover}\")"
    else:
        return f"[{name}]({url})"



# print(tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!"))
# print(tidy_link("https://www.google.com", "Google", "Google Search"))
# print(tidy_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!"))



"""7. Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.
Examples

pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }

Notes

    This is an oversimplification of the English language so no edge cases will appear.
    Only focus on whether or not to add an s to the ends of words.
    All tests will be valid."""


def pluralize(words: list):
    plural = set()
    for i in words:
        if words.count(i) > 1:
            plural.add(i + "s")
        else:
            plural.add(i)
    return plural




# print(pluralize(["cow", "pig", "cow", "cow"]))
# print(pluralize(["table", "table", "table"]))
# print(pluralize(["chair", "pencil", "arm"]))



"""8. Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.
Examples

censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"

censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")

censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?" """


def censor_string(txt, lst, char):
    for i in lst:
        txt = txt.replace(i.lower(), char * len(i))
    return txt
           

# print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
# print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
# print(censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*"))



