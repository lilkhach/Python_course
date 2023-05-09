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

# def rep_set(n):
#     if n == 0:
#         return []
#     else:
#         prev_set = rep_set(n-1)
#         return prev_set + [prev_set]


# print(rep_set(0) == [])

# print(rep_set(1) == [[]])

# print(rep_set(2) == [[], [[]]])

# print(rep_set(3) == [[], [[]], [[], [[ ]]]])





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

Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number 
(e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

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

# def arithmetic_operation(nums: str):
#     num = nums.split(" ")
#     if num[1] == "//":
#         if int(num[2]) == 0:
#             return("-1")
#         else:
#             return(int(num[0]) // int(num[2]))
#     elif num[1] == "+":
#         return(int(num[0]) + int(num[2]))
#     elif num[1] == "*":
#         return(int(num[0]) * int(num[2]))
#     elif num[1] == "-":
#         return(int(num[0]) - int(num[2]))
    

# print(arithmetic_operation("12 + 12"))# ➞ 24 // 12 + 12 = 24

# print(arithmetic_operation("12 - 12")) #➞ 24 // 12 - 12 = 0

# print(arithmetic_operation("12 * 12")) #➞ 144 // 12 * 12 = 144

# print(arithmetic_operation("12 // 0")) #➞ -1 // 12 / 0 = -1


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




"""6. Combined Consecutive Sequence

Write a function that returns True if two arrays, when combined, form a consecutive sequence. 
A consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.
Examples

consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

consecutive_combo([44, 46], [45]) ➞ True

Notes

    The input lists will have unique values.
    The input lists can be in any order."""


# def consecutive_combo(lst1, lst2):
#     comb_list = lst1 + lst2
#     start = min(comb_list)
#     end = max(comb_list)
#     new_lst = list(range(start, end+1))
#     for i in new_lst:
#         if i not in comb_list:
#             return False
#     else:
#         return True



# print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]) == True)

# print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) == False)

# print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) == False)

# print(consecutive_combo([44, 46], [45]) == True)




"""7. Tallest Skyscraper

A city skyline can be represented as a 2-D list with 1s representing buildings. 
In the example below, the height of the tallest building is 4 (second-most right column).

[[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]

Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.
Examples

tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 3

tallest_skyscraper([
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 4

tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 2"""




"""8. Sales by Match

Given a list of integers representing the color of each sock, determine how many pairs of socks with matching colors there are. For example, there are 7 socks with colors [1, 2, 1, 2, 1, 3, 2]. There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

Create a function that returns an integer representing the number of matching pairs of socks that are available.
Examples

sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) ➞ 3

sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]) ➞ 4

sock_merchant([]) ➞ 0"""




"""9. Remove The Word!

Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.
Examples

remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]

remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []

Notes

    If number of times a letter appears in the list is greater than the number of times the letter appears in the string, the extra letters should be left behind (see example #2).
    If all the letters in the list are used in the string, the function should return an empty list (see example #3)."""



"""10. Geometry 3: Perimeter of a Triangle

Write a function that takes the coordinates of three points in the form of a 2d array and returns the perimeter of the triangle. The given points are the vertices of a triangle on a two-dimensional plane.
Examples

perimeter([[15, 7], [5, 22], [11, 1]]) ➞ 47.08

perimeter([[0, 0], [0, 1], [1, 0]]) ➞ 3.41

perimeter([[-10, -10], [10, 10 ], [-10, 10]]) ➞ 68.28

Notes

    The given points always create a triangle.
    The numbers in the argument array can be positive or negative.
    Output should have 2 decimal places
    This challenge is easier than it looks."""



"""11. Majority Vote

Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).
Examples

majority_vote(["A", "A", "B"]) ➞ "A"

majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"

majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None

Notes

    The frequency of the majority element must be strictly greater than 1/2.
    If there is no majority element, return None.
    If the list is empty, return None."""




"""12. Pluralize!

Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.
Examples

pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }

Notes

    This is an oversimplification of the English language so no edge cases will appear.
    Only focus on whether or not to add an s to the ends of words.
    All tests will be valid."""




"""13. Secret Function 4.0

Create a function based on the input and output. Look at the examples, there is a pattern.
Examples

secret("p.one.two.three") ➞ "<p class='one two three'></p>"

secret("p.one") ➞ "<p class='one'></p>"

secret("p.four.five") ➞ "<p class='four five'></p>"

Notes

Input is a string."""




"""14. Count and Identify Data Types

Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list.

List order is:

[int, str, bool, list, tuple, dictionary]

Examples

count_datatypes(1, 45, "Hi", False) ➞ [2, 1, 1, 0, 0, 0]

count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) ➞ [3, 0, 0, 1, 1, 0]

count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) ➞ [2, 2, 3, 1, 0, 2]

count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]) ➞ [2, 0, 1, 2, 2, 0]

Notes

If no arguments are given, return [0, 0, 0, 0, 0, 0]"""




"""15. How Many Unique Styles?

There are many different styles of music and many albums exhibit multiple styles. Create a function that takes a list of musical styles from albums and returns how many styles are unique.
Examples

unique_styles([
  "Dub,Dancehall",
  "Industrial,Heavy Metal",
  "Techno,Dubstep",
  "Synth-pop,Euro-Disco",
  "Industrial,Techno,Minimal"
]) ➞ 9

unique_styles([
  "Soul",
  "House,Folk",
  "Trance,Downtempo,Big Beat,House",
  "Deep House",
  "Soul"
]) ➞ 7"""





"""List of Multiples

Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num until the list length reaches length.
Examples

list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]

list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]

Notes

Notice that num is also included in the returned list."""

# def list_of_multiples(num, length):
#     x = []
#     for i in range(1, length+1):
#         x.append(num * i)
#     return x


# print(list_of_multiples(12, 10))



"""7. """



