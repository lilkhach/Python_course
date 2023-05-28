"""1. Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.
Examples

remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]

remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []

Notes

    If number of times a letter appears in the list is greater than the number of times the letter appears in the string, the extra letters should be left behind (see example #2).
    If all the letters in the list are used in the string, the function should return an empty list (see example #3). """

def remove_letters(lst: list, st: str):
    
    for i in st:
        if i in lst:
            lst.remove(i)
    return lst


# print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") == ["w"])

# print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") == ["b", "g", "w"])

# print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") == [])




"""2. Create a function based on the input and output. Look at the examples, there is a pattern.
Examples

secret("p.one.two.three") ➞ "<p class='one two three'></p>"

secret("p.one") ➞ "<p class='one'></p>"

secret("p.four.five") ➞ "<p class='four five'></p>"

Notes

Input is a string."""



def secret(inp: str):


  inpl = inp.split(".")
  inps = " ".join(inpl[1:])

  return f"<{inpl[0]} class='{inps}'></p>"
    


# print(secret("p.one.two.three") == "<p class='one two three'></p>")

# print(secret("p.one") == "<p class='one'></p>")

# print(secret("p.four.five") == "<p class='four five'></p>")



"""3. Create a function which takes in an encoded string and returns a dictionary according to the following example:
Examples

parse_code("John000Doe000123") ➞ {
  "first_name": "John",
  "last_name": "Doe",
  "id": "123"
}

parse_code("michael0smith004331") ➞ {
  "first_name": "michael",
  "last_name": "smith",
  "id": "4331"
}

parse_code("Thomas00LEE0000043") ➞ {
  "first_name": "Thomas",
  "last_name": "LEE",
  "id": "43"
}

Notes

    The string will always be in the same format: first name, last name and id with zeros between them.
    id numbers will not contain any zeros.
    Bonus: Try solving this using RegEx."""



def parse_code(data: str):

  for i in data:
    if i == "0":
      datan = data.replace("0", " ").split()

  dict_keys = ["first_name", "last_name", "id"]
  my_dict = {key: None for key in dict_keys}

  my_dict["first_name"] = datan[0]
  my_dict["last_name"] = datan[1]
  my_dict["id"] = datan[2]

  return my_dict



# print(parse_code("John000Doe000123") == {
#   "first_name": "John",
#   "last_name": "Doe",
#   "id": "123"
# })

# print(parse_code("michael0smith004331") == {
#   "first_name": "michael",
#   "last_name": "smith",
#   "id": "4331"
# })

# print(parse_code("Thomas00LEE0000043") == {
#   "first_name": "Thomas",
#   "last_name": "LEE",
#   "id": "43"
# })


"""4. "Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one, saying the phrase 
"Loves me" and "Loves me not" when determining whether the one that they love, loves them back.

Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, 
and return the last phrase in all caps. Remember to put a comma and space between phrases.
Examples

loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"

loves_me(6) ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"

loves_me(1) ➞ "LOVES ME"

Notes

    Remember to return a string.
    The first phrase is always "Loves me"."""


def loves_me(petals: int):
    love = ["Loves me", "Loves me not"]
    result = []
    for i in range(petals):
        result.append(love[i%2])
    result[-1] = result[-1].upper()
    return ", ".join(result)


# print(loves_me(3) == "Loves me, Loves me not, LOVES ME")

# print(loves_me(6) == "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT")

# print(loves_me(1) == "LOVES ME")


"""5. Write a function that takes a list of numbers and returns a list with two elements:

    The first element should be the sum of all even numbers in the list.
    The second element should be the sum of all odd numbers in the list.

Example

sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])

sum_odd_and_even([0, 0]) ➞ [0, 0])

Notes

Count 0 as an even number."""

# def sum_odd_and_even(nums: list):
 
#    even_sum = 0
#    odd_sum = 0
#    for i in (nums):
#     if i % 2 == 0:
#       even_sum += i
#     else:
#        odd_sum += i
#    return [even_sum, odd_sum]

# print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))


"""6. Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects like 
{ "name": "John", "top_note": 5 }.
Examples

top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }

top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }

top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }"""


# def top_note(obj: dict):
#    obj["notes"] = max(obj["notes"])
#    return obj

# print(top_note({ "name": "Zygmund", "notes": [1, 2, 3] }))



"""7. Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
Examples

format_date("11/12/2019") ➞ "20191211"

format_date("12/31/2019") ➞ "20193112"

format_date("01/15/2019") ➞ "20191501"

Notes

Return value should be a string."""


# def format_date(date: str):
#    new_lst = date.split("/")[::-1]
#    new_format = "".join(new_lst)
#    return new_format
   


# print(format_date("12/31/2019"))


print("John" > "Jhon")
print("Emma" < "Emm")
