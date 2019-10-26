n = int(input())
s = set(map(int, input().split()))
commands = int(input())
for i in range(commands):
    lst = [i for(i) in input().split()]
    if(lst[0] == "pop"):
        s.pop()
    if(lst[0] == "discard"):
        s.discard(int(lst[1]))
    if(lst[0] == "remove"):
        s.remove(int(lst[1]))
print(sum(s))