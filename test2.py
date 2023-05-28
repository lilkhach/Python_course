
# how to create lists in list

result = []
for i in range(1, 11):
    x = []
    for j in range(1, 11):
        x.append(i*j)
    result.append(x)
print(result)


