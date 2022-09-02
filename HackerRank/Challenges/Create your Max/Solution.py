T=int(input())
String=input()
number=[]
for i in String:
    number.append(i)
number.sort()

out=""
for i in number:
    out+=i
print(out[::-1])