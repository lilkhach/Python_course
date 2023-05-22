"""1. Magic Function

Create a class with a few functions like these examples.

    magic.replace("string", 'char', char') is a function that replaces all of the specified characters with different specified characters.
    magic.str_length("string") is a function that returns the length of the string.
    magic.trim(" string ") is a function that returns a string with truncated spaces at both the beginning and end.
    magic.list_slice(list, tuple) is a function that returns the items in the list that are between the specified indexes. 
    If the length of the new list is 0, return -1.

Examples

magic.replace("AzErty-QwErty", "E", "e") ➞ "Azerty-Qwerty"

magic.str_length("hello world") ➞ 11

magic.trim("      python is awesome      ") ➞ "python is awesome"

magic.list_slice([1, 2, 3, 4, 5], (2, 4)) ➞ [ 2, 3, 4 ]"""



# class Magic:
#     def replace(self, expression: str, char_1: str, char_2: str):
#         return expression.replace(char_1, char_2)
    
#     def str_length(self, word: str):
#         return len(word)
    
#     def trim(self, new_string: str):
#         return new_string.strip()
    
#     def list_slice(self, arr: list, tup: tuple):
#         start_index = min(tup)-1
#         end_index = max(tup) 

#         if start_index >= end_index:
#             return -1

#         sliced_items = arr[start_index:end_index]
#         if len(sliced_items) == 0:
#             return -1

#         return sliced_items


# magic = Magic()
# print(magic.replace("AzErty-QwErty", "E", "e") == "Azerty-Qwerty")
# print(magic.str_length("hello world") == 11)
# print(magic.trim("      python is awesome      ") == "python is awesome")
# print(magic.list_slice([1, 2, 3, 4, 5], (2, 4)) == [ 2, 3, 4 ])




"""2. Ones, Threes and Nines (Version #2)

Given an integer between 0 and 26, make a variable (self.answer). That variable would be assigned to a string in this format:

"nines:your answer, threes:your answer, ones:your answer"

You need to find out how many ones, threes, and nines it would at least take for the number of each to add up to the given integer
when multiplied by one, three or nine (depends).
Examples

ones_threes_nines(10) ➞ "nines:1, threes:0, ones:1"

ones_threes_nines(15) ➞ "nines:1, threes:2, ones:0"

ones_threes_nines(22) ➞ "nines:2, threes:1, ones:1"

Notes

    Each of the ones, threes or nines could only be either 0, 1 or 2.
    You must use a class.
    After the comma, you must put a space.
    See version #1 of this series."""


# class Ones_threes_nines:
#     def __init__(self, n: int):
#         self.nines = n // 9
#         self.threes = (n - (self.nines * 9)) // 3
#         self.ones = (n - (self.nines * 9) - (self.threes * 3))
#         self.result = f"nines:{self.nines}, threes:{self.threes}, ones:{self.ones}"
    
# ones_threes_nines = Ones_threes_nines(10)
# print(ones_threes_nines.result == "nines:1, threes:0, ones:1")

# ones_threes_nines = Ones_threes_nines(15)
# print(ones_threes_nines.result == "nines:1, threes:2, ones:0")

# ones_threes_nines = Ones_threes_nines(22)
# print(ones_threes_nines.result == "nines:2, threes:1, ones:1")



"""3. To the Right, to the Right!

Create a class that imitates a select screen. For simplicity, the cursor can only move right!

In the display method, return a string representation of the list, 
but with square brackets around the currently selected element. Also, create the method to_the_right, which moves the cursor one element to the right.

The cursor should start at index 0.
Examples

menu = Menu([1, 2, 3])
menu.display() ➞ "[[1], 2, 3]"

menu.to_the_right()
menu.display() ➞ "[1, [2], 3]"

menu.to_the_right()
menu.display() ➞ "[1, 2, [3]]"

menu.to_the_right()
menu.display() ➞ "[[1], 2, 3]"

Notes

The cursor should wrap back round to the start once it reaches the end."""

# x = [1, 2, 3]
# for i in x:
#     print(x[0])


"""4. Employee Parsing

In the class Employee, implement the instance attributes as firstname, lastname and salary.

Create the method from_string() which parses a string containing these attributes and assigns them to the correct properties. 
Properties will be separated by a dash.
Examples

emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")

emp1.firstname ➞ "Mary"

emp1.salary ➞ 60000

emp2.firstname ➞ "John"

emp2.salary ➞ 55000

Notes

    The salary is an integer.
    Check the Resources for some helpful tutorials on how to do this."""




"""5. People Sort

Given a list of people objects, create a function that sorts the list by an attribute name. The attribute to sort by will be given as a string.

The Person class will only include these attributes in the following order:

    firstname
    lastname
    age

Examples

p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)

people_sort([p1, p2, p3], "firstname") ➞ [p2, p1, p3]
# Alice, Michael, Zoey

people_sort([p1, p2, p3], "lastname") ➞ [p3, p1, p2]
# Jones, Smith, Waters

people_sort([p1, p2, p3], "age") ➞ [p2, p3, p1]
# 21, 29, 40

Notes

    Sort the list in ASCENDING order.
    All objects will be valid."""


class Person:
    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def people_sort(self, people, keyword):
        if keyword == "firstname":
            return sorted(people)
        elif keyword 


# x = ("Michael", "Alice", "Zoey")

# print(sorted(x))


"""6. Wait... Who Am I?

Hello there, I... seem to not remember who I am, my memories is all... cloudy, although maybe if I could piece it together...

Oh! Maybe you could help me make a class that helps me remember things. 
Maybe a method called add that would add to my memory if I would recall things and a remember method that would let me recall a specific memory.

But you have to make add more flexible, I might recall many things in an instant or only one that I would forget again.
Examples :D

# add method doesn't return anything.
memories.add(name="Shane", gender="M", catch_phrase="bazinga")

memories.add(work="None", love_life=0)

memories.add(adress="car")

memories.remember("work") ➞ "None"

memories.remember("gender") ➞ "M"

# If memory was not added, return False
memories.remember("lover") ➞ False

Notes

The add method should be able to handle any number of arguments."""





"""7. Shiritori Game

This challenge is an English twist on the Japanese word game Shiritori. The basic premise is to follow two rules:

    First character of next word must match last character of previous word.
    The word must not have already been said.

Below is an example of a Shiritori game:

["word", "dowry", "yodel", "leader", "righteous", "serpent"]  #valid!

["motive", "beach"]  # invalid! - beach should start with "e"

["hive", "eh", "hive"]  # invalid! - "hive" has already been said

Write a Shiritori class that has two instance variables:

    words: a list of words already said.
    game_over: a boolean that is true if the game is over.

and two instance methods:

    play: a method that takes in a word as an argument and checks if it is valid (the word should follow rules #1 and #2 above).
        If it is valid, it adds the word to the words list, and returns the words list.
        If it is invalid (either rule is broken), it returns "game over" and sets the game_over boolean to true.

    restart: a method that sets the words list to an empty one [] and sets the game_over boolean to false. It should return "game restarted".

Examples

my_shiritori = Shiritori()

my_shiritori.play("apple") ➞ ["apple"]
my_shiritori.play("ear") ➞ ["apple", "ear"]
my_shiritori.play("rhino") ➞ ["apple", "ear", "rhino"]
my_shiritori.play("corn") ➞ "game over"

# Corn does not start with an "o".

my_shiritori.words ➞  ["apple", "ear", "rhino"]

# Words should be accessible.

my_shiritori.restart() ➞ "game restarted"
my_shiritori.words ➞ []

# Words list should be set back to empty.

my_shiritori.play("hostess") ➞ ["hostess"]
my_shiritori.play("stash") ➞ ["hostess", "stash"]
my_shiritori.play("hostess") ➞ "game over"

# Words cannot have already been said.

Notes

    Note: The play method should not add an invalid word to the words list.
    You don't need to worry about capitalization or white spaces for the inputs for the play method.
    The play method will only take in single arguments as inputs.
    Read more about Shiritori in the Resources tab."""





"""8. Employee Class with Keywords

Create a class Employee that will take a full name as argument, as well as a set of none, one or more keywords. Each instance should have a name and a lastname attribute plus one more attribute for each of the keywords, if any.
Examples

john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")

john.name ➞ "John"
mary.lastname ➞ "Major"
richard.height ➞ 178
giancarlo.nationality ➞ "Italian"

Notes

    First and last names will be separated by whitespace. The test will not include any middle names or initials.
    The value of the keywords can be an int, a str or a list."""