"""1. Create a function which returns the number of true values there are in an array.

Examples
countTrue([true, false, false, true, false]) ➞ 2

countTrue([false, false, false, false]) ➞ 0

countTrue([]) ➞ 0
Notes
Return 0 if given an empty array.
All array items are of the type bool (true or false). """


def countTrue(array: list):
    count = 0
    for i in array:
        if i:
            count += 1
    return count



print(countTrue([True, False, False, True, False]) == 2)

print(countTrue([False, False, False, False]) == 0)

print(countTrue([]) == 0)



"""2. Create a function that validates whether a number n is within the bounds of lower and upper. Return false if n is not an integer.

Examples
intWithinBounds(3, 1, 9) ➞ true

intWithinBounds(6, 1, 6) ➞ false

intWithinBounds(4.5, 3, 8) ➞ false
Notes
The term "within bounds" means a number is considered equal or greater than a lower bound and lesser (but not equal) to an upper bound, (see example #2).
Bounds will be always given as integers. """



def intWithinBounds(n, lower, upper):

    if not isinstance(n, int):
        return False
    return lower <= n < upper



print(intWithinBounds(3, 1, 9) == True)

print(intWithinBounds(6, 1, 6) == False)

print(intWithinBounds(4.5, 3, 8) == False)



"""3. Create a function that takes three values:

h hours
m minutes
s seconds
Return the value that's the longest duration.

Examples
longestTime(1, 59, 3598) ➞ 1

longestTime(2, 300, 15000) ➞ 300

longestTime(15, 955, 59400) ➞ 59400 """


def longestTime(h, m, s):

    long_dur = max(h * 3600, m * 60, s)
    return long_dur


print(longestTime(1, 59, 3598)) #== 1)

print(longestTime(2, 300, 15000)) #== 300)

print(longestTime(15, 955, 59400) == 59400)



"""4. Create a function that takes the month and year (as integers) and returns the number of days in that month.

Examples
days(2, 2018) ➞ 28

days(4, 654) ➞ 30

days(2, 200) ➞ 28

days(2, 1000) ➞ 28
Notes
Don't forget about leap years! """



def day_count (month: int, year: int):
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0):
            return 29  # leap year
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31



print(day_count(2, 2024) == 29)

print(day_count(4, 654) == 30)

print(day_count(2, 200) ==28)

print(day_count(2, 1000) == 28)



"""5. Create a function that takes a string and censors words over four characters with *.

Examples
censor("The code is fourty") ➞ "The code is ******"

censor("Two plus three is five") ➞ "Two plus ***** is five"

censor("aaaa aaaaa 1234 12345") ➞ "aaaa ***** 1234 *****"
Notes
Don't censor words with exactly four characters.
If all words have four characters or less, return the original string.
The amount of * is the same as the length of the word. """



def censor(exp: str):
    lst_exp = exp.split()
    new_exp = []
    for i in lst_exp:
        if len(i) > 4:
            new_word = "*" * len(i)
            new_exp.append(new_word)
        else:
            new_exp.append(i)
    return " ".join(new_exp)



print(censor("The code is fourty") == "The code is ******")

print(censor("Two plus three is five") == "Two plus ***** is five")

print(censor("aaaa aaaaa 1234 12345") == "aaaa ***** 1234 *****")




"""6. Given a sentence, create a function that replaces every "a" as an article with "an absolute". 
It should return the same string without any change if it doesn't have any "a".

Examples
absolute("I am a champion!!!") ➞ "I am an absolute champion!!!"

absolute("Such an amazing bowler.") ➞ "Such an amazing bowler."

absolute("A man with no haters.") ➞ "An absolute man with no haters."
Notes
Watch for uppercase letters as shown in example #3. """


def absolute(sent: str):

    lst_sent = sent.split()

    for i in range(len(lst_sent)):  

        if lst_sent[i] == "a":
            lst_sent[i] = "an absolute"  

        elif lst_sent[i] == "A":
            lst_sent[i] = "An absolute"  

    return " ".join(lst_sent)
        

print(absolute("I am a champion!!!") == "I am an absolute champion!!!")

print(absolute("Such an amazing bowler.") == "Such an amazing bowler.")

print(absolute("A man with no haters.") == "An absolute man with no haters.")




"""7. Return an Array of Subarrays
Write a function that takes three arguments (x, y, z) and returns an array containing x subarrays (e.g. [[], [], []]), each containing y number of item z.

x Number of subarrays contained within the main array.
y Number of items contained within each subarray.
z Item contained within each subarray.

Examples
matrix(3, 2, 3) ➞ [[3, 3], [3, 3], [3, 3]]

matrix(2, 1, "edabit") ➞ [["edabit"], ["edabit"]]

matrix(3, 2, 0) ➞ [[0, 0], [0, 0], [0, 0]]
Notes
The first two arguments will always be integers.
The third argument is either a string or an integer. """


def matrix(x, y, z):

    output = []

    for i in range(x):
        subarray = [z] * y
        output.append(subarray)

    return output


print(matrix(3, 2, 3) == [[3, 3], [3, 3], [3, 3]])

print(matrix(2, 1, "edabit") == [["edabit"], ["edabit"]])

print(matrix(3, 2, 0) == [[0, 0], [0, 0], [0, 0]])



"""8. Given a string of numbers separated by a comma and space, return the product of the numbers.

Examples
multiplyNums("2, 3") ➞ 6

multiplyNums("1, 2, 3, 4") ➞ 24

multiplyNums("54, 75, 453, 0") ➞ 0

multiplyNums("10, -2") ➞ -20
Notes
Bonus: Try to complete this challenge in one line! """


def multiplyNums(string):

    return eval("*".join(string.split(", ")))



print(multiplyNums("2, 3") == 6)

print(multiplyNums("1, 2, 3, 4") == 24)

print(multiplyNums("54, 75, 453, 0") == 0)

print(multiplyNums("10, -2") == -20)



"""9. Create a function that takes a string road and returns the car that's in first place. 
The road will be made of "=", and cars will be represented by letters in the alphabet.

Examples
firstPlace("====b===O===e===U=A==") ➞ "A"

firstPlace("e==B=Fe") ➞ "e"

firstPlace("proeNeoOJGnfl") ➞ "l"
Notes
Return "No car available" if there is no car on the road and "No road available" if there is no road."""


def firstPlace(road_string):
    if not road_string:
        return "No road available"  
    elif all(i == '=' for i in road_string):
        return "No car available"
    
    return road_string.replace("=", "")[-1]



print(firstPlace("====b===O===e===U=A=="))
print(firstPlace("e==B=Fe"))
print(firstPlace(""))


"""10. Create a function that takes an array of numbers between 1 and 10 (excluding one number) and returns the missing number.

Examples
missingNum([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5

missingNum([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10

missingNum([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
Notes
The array of numbers will be unsorted (not in order).
Only one number will be missing."""



def missingNum(array):

    full_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    missing_number = set(full_arr) - set(array)
    return int(missing_number.pop())


print(missingNum([7, 2, 3, 6, 5, 9, 1, 4, 8]))