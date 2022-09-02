d={}
number = input()
string=input()
string1="abcdefghijklmnopqrstuvwxyz"
for i in string1:
    d[i]=0
for i in string:
    if i in d:
        d[i]+=1

for i in sorted(d):
    print(f"{i}: {d[i]}")
