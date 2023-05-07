"""1. Natural Emptiness

In abstract set theory, a construction due to von Neumann represents the natural numbers by sets, as follows:

    0 = [ ] is the empty set
    1 = 0 ∪ [ 0 ] = [ 0 ] = [ [ ] ]
    2 = 1 ∪ [ 1 ] = [ 0, 1 ] = [ [ ], [ [ ] ] ]
    n = n−1 ∪ [ n−1 ] = ...

Write a function that receives an integer n and produces the representing set.
Examples

rep_set(0) ➞ []

rep_set(1) ➞ [[]]

rep_set(2) ➞ [[], [[]]]

rep_set(3) ➞ [[], [[]], [[], [[ ]]]]

Notes

    Make sure to use list brackets [,].
    Technically we should use set brackets {,} instead, but Python doesn't approve.
    A neat feature of this representation is that n < m precisely if the set representing n is contained in the set representing m.""" 






"""2. Imaginary Coding Interview

Create a function to check if a candidate is qualified in an imaginary coding interview of an imaginary tech startup.

The criteria for a candidate to be qualified in the coding interview is:

    The candidate should have complete all the questions.
    The maximum time given to complete the interview is 120 minutes.
    The maximum time given for very easy questions is 5 minutes each.
    The maximum time given for easy questions is 10 minutes each.
    The maximum time given for medium questions is 15 minutes each.
    The maximum time given for hard questions is 20 minutes each.

If all the above conditions are satisfied, return "qualified", else return "disqualified".

You will be given a list of time taken by a candidate to solve a particular question and the total time taken by the candidate to complete the interview.

Given a list , in a true condition will always be in the format [very easy, very easy, easy, easy, medium, medium, hard, hard].

The maximum time to complete the interview includes a buffer time of 20 minutes.
Examples

interview([5, 5, 10, 10, 15, 15, 20, 20], 120) ➞ "qualified"

interview([2, 3, 8, 6, 5, 12, 10, 18], 64) ➞  "qualified"

interview([5, 5, 10, 10, 25, 15, 20, 20], 120) ➞ "disqualified"
# Exceeded the time limit for a medium question.

interview([5, 5, 10, 10, 15, 15, 20], 120) ➞ "disqualified"
# Did not complete all the questions.

interview([5, 5, 10, 10, 15, 15, 20, 20], 130) ➞ "disqualified"
# Solved all the questions in their respected time limits but exceeded the total time limit of the interview.

Notes

Try to solve the problem using only list methods.""" 


# def interview(time_list, total_time):
#     if len(time_list) != 8:
#         return "disqualified"
#     elif total_time > 120:
#         return "disqualified"
#     for i in range(2):
#         if time_list[i] > 5:
#             return "disqualified"
#     for i in range(2, 4):
#         if time_list[i] > 10:
#             return "disqualified"
#     for i in range(4, 6):
#         if time_list[i] > 15:
#             return "disqualified"
#     for i in range(6, 8):
#         if time_list[i] > 20:
#             return "disqualified"
    
#     return "qualified"
    

# print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120) == "qualified")

# print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64) ==  "qualified")

# print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120) == "disqualified")
# # Exceeded the time limit for a medium question.

# print(interview([5, 5, 10, 10, 15, 15, 20], 120) == "disqualified")
# # Did not complete all the questions.

# print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130) == "disqualified")




"""3. Basic Arithmetic Operations on a String Number

Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

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





"""4. Create a function that takes a string as an argument and returns the Morse code equivalent.
Examples

encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."

encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"

This dictionary can be used for coding:

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

Notes

    Ouput should be International Morse Code, and use the standard conventions for symbols not defined inside the ITU recommendation (see Resources).
    Input value can be lower or upper case.
    Input string can have digits.
    Input string can have some special characters (e.g. comma, colon, apostrophe, period, question mark, exclamation mark).
    One space " " is expected after each character, except the last one."""


# def encode_morse(st: str):
#     st = st.upper()
#     code = []
#     char_to_dots = {
#   'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#   'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#   'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
#   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#   '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#   '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
#   ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
#   '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
# }
#     for i in st:
#         if i in char_to_dots:
#             code.append(char_to_dots[i])
#     return " ".join(code)
        

    
# print(encode_morse("EDABBIT CHALLENGE") == ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. .")

# print(encode_morse("HELP ME !") == ".... . .-.. .--.   -- .   -.-.--")




"""5. Mahjong Tiles

Your goal is to create a function that returns a list with a string for each of the 108 tiles in the following format:

"rank suit"

Where rank is a number from 1 to 9 and suit is one of the three suits (tong, tiao, wan), both written in the pinyin transcription of
Mandarin Chinese (for numbers see table below).
Number	Character	Pinyin
1	一	yi
2	二	er
3	三	san
4	四	si
5	五	wu
6	六	liu
7	七	qi
8	八	ba
9	九	jiu

Three of the tiles have special names. Each of the 4 copies of these tiles should be represented by their names only (no suit, no rank):

    One of tong is called bing gan (饼干, cookie)
    Two of tong is called yan jing (眼镜, glasses)
    One of tiao is called ji (鸡, chicken)

Examples of tiles

Five of tong ➞ "wu tong"

Seven of wan ➞ "qi wan"

One of tiao ➞ "ji"

Three of tiao ➞ "san tiao"

Notes

    Don't forget to include 4 copies of each tile.
    Don't forget to substitute the tiles with special names.
    You can return the tiles in any order."""



"""6. List of Multiples

Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num until the list length reaches length.
Examples

list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]

list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]

Notes

Notice that num is also included in the returned list."""

def list_of_multiples(num, length):
    x = []
    for i in range(1, length+1):
        x.append(num * i)
    return x
# def list_of_multiples(num, length):
#     return [num * i for i in range(1, length+1)]


print(list_of_multiples(12, 10))



