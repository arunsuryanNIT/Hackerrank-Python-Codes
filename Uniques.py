numbers = [int (i) for i in input().split()]
unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)