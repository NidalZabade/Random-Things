T=int(input())
String=input()
count=0
while "116" in String:
    count+=String.count("116")
    String=String.replace("116","")
print(count)