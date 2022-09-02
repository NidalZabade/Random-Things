T=int(input())
for i in range(T):
    N=int(input())
    String=input()
    state=[]
    state.append(String.count("+"))
    state.append(String.count("-"))
    print(*state,sep=" ")