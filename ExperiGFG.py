import math
def nearestPower(a,b):
    x=math.floor(math.log(b,a))
    return a**x

var = nearestPower(34, 100)
print(var)