m = int(input())
lst1 = (int (i) for i in input().split())
n = int(input())
lst2 = (int (j) for j in input().split())
setOne = set(lst1)
setTwo = set(lst2)
s = (setOne.difference(setTwo)). union((setTwo.difference(setOne)))
lst3 = list(s)
lst3.sort()
for i in lst3:
    print(i)