from math import gcd as __gcd
def getCount(a, n):
 
    gcd = 0
    for i in range(n):
        gcd = __gcd(gcd, a[i])
 
    cnt = 0
 
    for i in range(1, gcd + 1):
        if i * i > gcd:
            break
        if (gcd % i == 0):
 
            if (i * i == gcd):
                cnt += 1
 
            else:
                cnt += 2
 
    return cnt
 
T=int(input())
a=list(map(int,input().split()))


 
print(getCount(a, T))
