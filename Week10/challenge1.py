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

    