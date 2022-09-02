n=int(input())
number=input()
numbers=[]
for i in number:
    numbers.append(int(i))
numbers.sort()


out=""
for i in numbers:
    if i==0:
        continue
    else:
        out=out+str(i)
        numbers.remove(i)
        break

for i in numbers:
    out=out+str(i)

print((out))
