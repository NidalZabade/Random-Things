# Rantisi this semester is studying very well to be in the honor list, but to be in the honor list he must meet certain conditions, given the N courses of this semester and for each course x(i), g(i)

x(i): the course hours\
g(i): the grade of this course
##
#### can you tell rantisi if he is in the honor list this semester or if he should study more next semester. condition of honor list: x(i) >= 80, avg >= 85, number of hours >= 15, and number of courses >= 4

#### but the semester isn't done yet so we will get T scenario to answer it.
#
### Input Format

First Lint contain T : number of test Case

for each test case the first number is N: Number of courses

then N line contain x, g number oh hour and the grade for this course x(i) g(i)

### Constraints

100 >= T >= 1

8 >= N >= 1

4 >= x >= 1

99 >= g >= 50

### Output Format

print in new line for each test case "Honor list" wihout cotation if rantisi in the honor list or "Try next semester" wihout cotation. **Please don't use break because the remain input will be in the next case so, you get wrong answer
#
* Sample Input 0

  2\
  5\
  3 90\
  3 90\
  3 80\
  3 99\
  3 88\
  4\
  4 90\
  3 80\
  1 77\
  1 87

* Sample Output 0

  Honor list\
  Try next semester

* Explanation 0

  In the first case all the condition is ture so rantisi will be in the honor list

  the second test case number of hour is less then 15 and theres one couse < 80
