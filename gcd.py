#brute force
def consecutive(a,b):
    if a>b:
        mn=a
    else:
        mn=b
    while(mn!=1):
        if a%mn ==0 and b%mn ==0:
            return mn
        mn -=1
    return -1

def middleschool(a,b):
    if a>b:
        mn=a
    else:
        mn=b
    res=1
    for i in range(2 ,mn+1):
        while(a%i==0 and b%i==0):
            res *=i
            a=a/i
            b=b/i
    return res
#obtimized
def euclids(a,b):
    temp=0
    while(b!=0):
        temp=b
        b=a%b
        a=temp
    return a

print(euclids(12,60))
print(middleschool(12,60))
print(consecutive(12,60))