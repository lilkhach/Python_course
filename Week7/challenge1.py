"""1. Write a function that takes a string name and a number num (either 0 or 1) and return "Hello" + name if num is 1, otherwise return "Bye" + name.

Examples
say_hello_bye("alon", 1) ➞ "Hello Alon"

say_hello_bye("Tomi", 0) ➞ "Bye Tomi"

say_hello_bye("jose", 0) ➞ "Bye Jose" """



def say_hello_bye(a: str, b: int):
    if b == 1:
        return f"Hello {a.capitalize()}"
    elif b == 0:
        return f"Bye {a.capitalize()}"
    else:
        return f"Wrong"
    
print(say_hello_bye("alon", 1) == "Hello Alon")

print(say_hello_bye("Tomi", 0) == "Bye Tomi")

print(say_hello_bye("jose", 0) == "Bye Jose")



"""2. Create a function that takes a list (slot machine outcome) and returns True if all elements in the list are identical, and False otherwise. 
The list will contain 4 elements.

Examples
test_jackpot(["@", "@", "@", "@"]) ➞ True

test_jackpot(["abc", "abc", "abc", "abc"]) ➞ True

test_jackpot(["SS", "SS", "SS", "SS"]) ➞ True

test_jackpot(["&&", "&", "&&&", "&&&&"]) ➞ False

test_jackpot(["SS", "SS", "SS", "Ss"]) ➞ False """



def test_jackpot(x: list):
    
    return all(i == x[0] for i in x)
    

print(test_jackpot(["@", "@", "@", "@"]) == True)

print(test_jackpot(["abc", "abc", "abc", "abc"]) == True)

print(test_jackpot(["SS", "SS", "SS", "SS"]) == True)

print(test_jackpot(["&&", "&", "&&&", "&&&&"]) == False)

print(test_jackpot(["SS", "SS", "SS", "Ss"]) == False)



"""3. Create a function that takes an array of hurdle heights and a jumper's jump height, and determine whether or not the hurdler can clear all the hurdles.

A hurdler can clear a hurdle if their jump height is greater than or equal to the hurdle height.

Examples
hurdle_jump([1, 2, 3, 4, 5], 5) ➞ True

hurdle_jump([5, 5, 3, 4, 5], 3) ➞ False

hurdle_jump([5, 4, 5, 6], 10) ➞ True

hurdle_jump([1, 2, 1], 1) ➞ False
Notes
Return True for the edge case of an empty array of hurdles. (Zero hurdles means that any jump height can clear them). """



def hurdle_jump(arr: list, h: int):
    if not arr:
        return True
    else:
        for i in arr:
            if i > h:
                return False
        return True
    

print(hurdle_jump([1, 2, 3, 4, 5], 5) == True)

print(hurdle_jump([5, 5, 3, 4, 5], 3) == False)

print(hurdle_jump([5, 4, 5, 6], 10) == True)

print(hurdle_jump([1, 2, 1], 1) == False)

print(hurdle_jump([], 1) == True)




"""4. Create a function that takes a number as its argument and returns a list of all its factors.

Examples
factorize(12) ➞ [1, 2, 3, 4, 6, 12]

factorize(4) ➞ [1, 2, 4]

factorize(17) ➞ [1, 17]
Notes
The input integer will be positive.
A factor is a number that evenly divides into another number without leaving a remainder. 
The second example is a factor of 12, because 12 / 2 = 6, with remainder 0."""



def factorize(x: int):
    factor = []
    for i in range(1, x+1):
        if x % i == 0:
            factor.append(i)
    return factor
        

print(factorize(12) == [1, 2, 3, 4, 6, 12])

print(factorize(4) == [1, 2, 4])

print(factorize(17) == [1, 17])




"""5. Create a function that returns the number of palindrome numbers in a specified range (inclusive).

For example, between 8 and 34, there are 5 palindromes: 8, 9, 11, 22 and 33. Between 1550 and 1552 there is exactly one palindrome: 1551.

Examples
count_palindromes(1, 10) ➞ 9

count_palindromes(555, 556) ➞ 1

count_palindromes(878, 898) ➞ 3
Notes
A palindrome number is a number which remains the same when its digits are reversed. 
For example, 2552 reversed is still 2552. The reflectional symmetry of this number makes it a palindromic number.
Single-digit numbers are trivially palindrome numbers."""



def count_palindromes(a: int, b: int):
    count = 0
    for i in range(a, b + 1):
        if str(i) == str(i)[::-1]: 
            count += 1
    return count

print(count_palindromes(1, 10) == 9)

print(count_palindromes(555, 556) == 1)

print(count_palindromes(878, 898) == 3)



"""6. Write a function that takes a string, breaks it up and returns it with vowels first, consonants second. 
For any character that's not a vowel (like special characters or spaces), treat them like consonants.

Examples
split("abcde") ➞ "aebcd"

split("Hello!") ➞ "eoHll!"

split("What's the time?") ➞ "aeieWht's th tm?"
Notes
Vowels are a, e, i, o, u.
Define a separate is_vowel() function for easier to read code (recommendation). """



def split(word: str):
    vowels = ["a", "e", "i", "o", "u"]
    vowel = []
    consonant = []
    for i in word:
        if i in vowels:
           vowel.append(i)
        else:
            consonant.append(i)
    else:
        consonant.append(i)
    new_word = "".join(vowel+ consonant)
    return new_word



print(split("abcde") == "aebcd")

print(split("Hello!") == "eoHll!")

print(split("What's the time?") == "aeieWht's th tm?").




"""7. Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.

Examples
hacker_speak("javascript is cool") ➞ "j4v45cr1pt 15 c00l"

hacker_speak("programming is fun") ➞ "pr0gr4mm1ng 15 fun"

hacker_speak("become a coder") ➞ "b3c0m3 4 c0d3r"
Notes
In order to work properly, the function should replace all "a"s with 4, "e"s with 3, "i"s with 1, "o"s with 0, and "s"s with 5. """



def hacker_speak(txt: str):
    keys = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5"}
    for i in txt:
        if i in keys:
            txt = txt.replace(i, keys[i])
    return txt


print(hacker_speak("javascript is cool") == "j4v45cr1pt 15 c00l")

print(hacker_speak("programming is fun") == "pr0gr4mm1ng 15 fun")

print(hacker_speak("become a coder") == "b3c0m3 4 c0d3r")




"""8. Create a function that takes an integer and returns it as an ordinal number. 
An Ordinal Number is a number that tells the position of something in a list, such as 1st, 2nd, 3rd, 4th, 5th, etc.

Examples
return_end_of_number(553) ➞ "553-RD"

return_end_of_number(34) ➞ "34-TH"

return_end_of_number(1231) ➞ "1231-ST"

return_end_of_number(22) ➞ "22-ND"

return_end_of_number(412) ➞ "412-TH" """


def return_end_of_number(num: int):
    if num % 100 in [11, 12, 13]:
        end = "TH"
    else:
        last_num = num % 10
        if last_num == 1:
            end = "ST"
        elif last_num == 2:
            end = "ND"
        elif last_num == 3:
            end = "RD"
        else:
            end = "TH"
    return f"{num}-{end}"


print(return_end_of_number(553) == "553-RD")

print(return_end_of_number(34) == "34-TH")

print(return_end_of_number(1231) == "1231-ST")

print(return_end_of_number(22) == "22-ND")

print(return_end_of_number(412) == "412-TH")



"""9. Create a function that converts Celsius to Fahrenheit and vice versa.

Examples
convert("35*C") ➞ "95*F"

convert("19*F") ➞ "-7*C"

convert("33") ➞ "Error"
Notes
Round to the nearest integer.
If the input is incorrect, return "Error".
For the formulae to convert back and forth, check the Resources tab. """




def convert(temp):
    if temp[-1] == "C":
        farenheit = round((int(temp[:-2]) * 9/5) + 32)
        return f"{farenheit}*F"
    elif temp[-1] == "F":
        celsius = round((int(temp[:-2]) - 32) * 5/9)
        return f"{celsius}*C"
    else:
        return "Error"
    
print(convert("35*C") == "95*F")

print(convert("19*F") == "-7*C")

print(convert("33") == "Error")



"""10. Create a function that finds the reverse complement of a ribonucleic acid (RNA) strand. 
The RNA will be represented as a string containing only the characters "A", "C", "G" and "U". 
Since RNA can only (canonically) allow pairings of A/U and G/C, the complement of an RNA would be as follows:

Original	Complement
"AAA"	"UUU"
"UUU"	"AAA"
"GGG"	"CCC"
"CCC"	"GGG"
Your function should find the complement on the right AND also reverse the resulting string.

Examples
reverse_complement("GUGU") ➞ "ACAC"

reverse_complement("UCUCG") ➞ "CGAGA"

reverse_complement("CAGGU") ➞ "ACCUG"
Notes
You can assume all input seqeuences will be valid. """


def reverse_complement(rna):
    complement_keys = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'} 
    complement = ""
    for i in rna:
        complement += complement_keys[i]
    return complement[::-1]


print(reverse_complement("GUGU") == "ACAC")

print(reverse_complement("UCUCG") == "CGAGA")

print(reverse_complement("CAGGU") == "ACCUG")




"""11. Create a function to perform basic arithmetic operations that includes addition, subtraction, 
multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

Here, we have 1 followed by a space, operator followed by another space and 2. 
For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

For example:

"15 // 0"  ➞ -1
Examples
arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24

arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0

arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144

arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1
Notes
All the inputs are only integers.
The operators are * - + and //.
Hint: Think about the single space that appears before and after the arithmetic operator."""

inp = "12 + 12"

def work(inp):
    inp = inp.split()
    a, b = int(inp[0]), int(inp[2])

    if inp[1] == "+":
        return a + b
    elif inp[1] == "-":
        return a-b
    elif inp[1] == "*":
        return a*b
    elif inp[1] == "//":
        if b == 0:
            return -1
        return a // b
    else:
        return "Not known operator"





"""12. Imagine you have three numbers: a, b and c. c is equal to either a or b, but you don't know which one.
Your task is to create a function that returns whatever number c isn't, out of a and b. So, if c is equal to a, return b, 
and if c is equal to b, return a. Here's what makes this challenge difficult: you can not use any if statements.

Examples:
swap(1, 0, 0) ➞ 1
#a = 1, b = 0, c = b
#return a

swap (1, 3, 1) ➞ 3
#a = 1, b = 3, c = a
#return b

swap(27, 31, 31) ➞ 27
#a = 27, b = 31, c = b
#return a

Notes:
-to prevent cheating, you also can't call any functions.
-c will always be equal to a or b.
-a will never be equal to b.
-a, b, and c will always be integers.
"""


def swap(a, b, c):
    return {a: b, b: a}[c]


print(swap(1, 0, 0) == 1)

print(swap(1, 3, 1) == 3)

print(swap(27, 31, 31) == 27)



def func(a:int, b:int, c:int):
    match c == b:
        case True:
            return a
        case False:
            return b
        
a, b, c = 1, 2, 2
print(func(a, b, c))


print((c == b) * a + (c == a) * b)
