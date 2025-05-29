import math
#brute force 
def lcm(a,b):
    maxim = max(a,b)
    while (True):
        if(maxim%a==0 and maxim%b==0):
            return maxim
        maxim +=1
    return
#Obtimised(log max)
def lcmugcd(a,b):
    return a*b // math.gcd(a,b)
print(lcm(2,3))
print(lcmugcd(2,3))