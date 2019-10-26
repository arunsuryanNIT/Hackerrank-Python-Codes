lst = []
n = int(input())
for i in range(0, n):
    lst2 = [i for i in input().split()]
    if(lst2[0] == "insert"):
        lst.insert(int(lst2[1]), int (lst2[2]))

    if(lst2[0] == "print"):
        print(lst)

    if(lst2[0] == "remove"):
        lst.remove(int(lst2[1]))

    if(lst2[0] == "append"):
        lst.append(int(lst2[1]))

    if(lst2[0] == "sort"):
        lst.sort()

    if(lst2[0] == "pop"):
        lst.remove(lst[len(lst) - 1])
    
    if(lst2[0] == "reverse"):
        lst.reverse()
