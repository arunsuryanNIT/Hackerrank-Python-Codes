n = int(input())
s = [int (i) for i in input().split()]
freq = {} 
for item in s: 
    if freq.get(item) != None: 
        freq[item] += 1
    else: 
        freq[item] = 1

for key, value in freq.items(): 
    if(value == 1):
        print(key)
