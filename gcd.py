#brute force
def consecutive(a,b):
    if a>b:
        min=a
    else:
        min=b
    while(min!=1):
        if a%min ==0 & b%min ==0:
            return min
        min -=1
    return -1

def middleschool(a,b):
    if a>b:
        mn=a
    else:
        mn=b
    res=1
    for i in range(2 ,mn):
        while(a%i==0 & b%i==0):
            res *=i
            a=a/i
            b=b/i
    return res
print(middleschool(12,60))