s = set(map(int, input().split()))
noofSets = int(input())
ans = True
for i in range(noofSets):
    anotherset = set(map(int, input().split()))
    if (s > anotherset) == False:
        ans = False
        break
print(ans)        