n = int(input())
s = set(map(int, input().split()))
noofSets = int(input())
for i in range(noofSets):
    opr, value = [i for i in input().split()]
    anotherset = set(map(int, input().split()))
    if(opr == "intersection_update"):
        s.intersection_update(anotherset)
    if(opr == "update"):
        s.update(anotherset)
    if(opr == "symmetric_difference_update"):
        s.symmetric_difference_update(anotherset)
    if(opr == "difference_update"):
        s.difference_update(anotherset)
    
print(sum(s))
