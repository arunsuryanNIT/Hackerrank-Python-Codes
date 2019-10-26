lst = [2, 3, 4, 5 , 6]
element = int(input("Enter element to insert\n"))
sizer = len(lst) + 1
for i in range (sizer, -1, -1):
    lst[i + 1] = lst[i]

lst[0] = element
print(lst)
