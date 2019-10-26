import math
def nearestPower(a,b):
    x=math.floor(math.log(b,a))
    xtemp=x+1
    n1=a**x
    n2=a**xtemp
    if(abs(n1-b)>abs(n2-b)):
       return n2
    else:
       return n1

var = nearestPower(3, 35)
