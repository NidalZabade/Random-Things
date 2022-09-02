# This semester, Rantisi is studying very well to be in the honor list, but to be in the honor list he must meet certain conditions, given the N courses of this semester and for each course x(i), g(i)
* x(i): the course hours
* g(i): the grade of this course Can you tell Rantisi if he will be in the honor list this semester or if he should study more next semester.

##

### Conditions for honor list:

All g(i) >= 80, avg >= 85, number of hours >= 15, and number of courses >= 4

### NOTE Rule is changed a little bit, there is a half honor with some modifications in the conditions:

All g(i) >= 80, avg >= 85, number of hours >= 12, and number of courses >= 3

So if he get half honor you will print Half honor list.

The semester still in progress, so we will get T scenarios to answer the problem.

### Input Format

First Lint contains T: number of test cases.

For each test case, the first number is N: Number of courses.

Then N line contain x, g number of hours and the grade for this course x(i) g(i)

### Constraints

100 >= T >= 1

8 >= N >= 1

4 >= x >= 1

99 >= g >= 50

### Output Format

Print in a new line for each test case "Honor list" if Rantisi is in the honor list or "Half honor list" if he get the half honor or "Try next semester", wihout cotation.

##

* Sample Input 0

  3\
  3\
  4 85\
  4 85\
  4 85\
  4\
  4 99\
  4 85\
  4 80\
  4 88\
  4\
  1 99\
  2 85\
  4 50\
  4 88

* Sample Output 0

  Half honor list
  Honor list
  Try next semester

* Explanation 0

  First case meet all condtions of half honor. Second case meet all condtions of honor. Third breaks two condtions 50< 80 and the number of hours < 12.
