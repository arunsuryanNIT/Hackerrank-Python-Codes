T = int(input())
for i in range(T):
    len1 = int(input())
    setA = set(map(int, input().split()))
    len2 = int(input())
    setB = set(map(int, input().split()))
    setC = setA.union(setB)
    if(setC == setB):
        print("True")
    else:
        print("False")
    