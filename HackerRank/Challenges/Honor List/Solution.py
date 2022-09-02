T = int(input())
for i in range(T):
    flag  = 0
    C = int(input())
    if C < 4:
        flag = 1
    hours = 0
    grades = 0
    for c in range(C):
        course = input()
        course = course.split(" ")
        if int(course[1]) < 80:
            flag  = 1
        hours += int(course[0])
        grades += int(course[1]) * int(course[0])
    average = grades / hours
    if average < 85:
        flag =  1
    if hours < 15:
        flag = 1
    print("Honor list") if not flag else print("Try next semester")
