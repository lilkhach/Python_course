"""4. Create a function that takes the age in years and returns the age in days. 1960 january 1
65 ➞ 23725
0 ➞ 0
20 ➞ 7300
"""


x = 1993

age = 2023 - x


print_text = "vayelir" * (age>=20 and age<=30) + "ush e" * (age>=30 and age<=40)

print(print_text)

