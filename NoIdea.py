m, n = [int(x) for x in input().split()] 
n_val = [int(i) for i in input().split()]
A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))
happiness = 0

for val in n_val:
    if val in A_set:
        happiness += 1
    elif val in B_set:
        happiness -= 1

print(happiness)
