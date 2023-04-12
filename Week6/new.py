# my_dict = {"apple": "fruit", "banana": "fruit", "carrot": "vegetable"}

# # Reversed dictionary
# reversed_dict = {v: k for k, v in my_dict.items()}

# # Printing reversed dictionary
# print(reversed_dict)


x = [1, 2, 4, 5]

new_x = []

for i in x:
    new_x.append(i**2)

new_x = [i**2 for i in x]

print(new_x)






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
