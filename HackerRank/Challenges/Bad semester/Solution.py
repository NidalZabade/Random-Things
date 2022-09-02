test=int(input())
for i in range(test):
    N,M,g,y=input().split(" ")
    total=int(N)*int(M)
    mod=total-int(g)
    if mod>=0:
        if int(y)==0:
            print(-1)
        else:
            print(mod)
    else:
        print(0)
