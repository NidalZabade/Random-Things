import math

def getdivisible(L, R, N): #1 10 1
    left, right = 0, 0
    if L%N == 0:
        left = L
    else:
        left = ((L+N)//N)*N
    if R%N == 0:
        right = R
    else:
        right = ((R)//N)*N
    return ((right - left)//N + 1)
ARRAY = input()
ARRAY = ARRAY.split(" ")
L = int(ARRAY[0])
R = int(ARRAY[1])
N = int(ARRAY[2])
M = int(ARRAY[3])
if max(N, M)%min(N, M) == 0:
    print(getdivisible(L, R, min(N, M)))
else:
    print(getdivisible(L, R, N)+getdivisible(L, R, M)-getdivisible(L, R, math.lcm(N,M)))