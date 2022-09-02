# Tala was recently checking some genetic code of DNA. A genetic code of DNA is represented by four characters 'A', 'G', 'C' and 'T'. In our problem we will represent it as a string consisting of these four characters.

#### She calls a subsequence of length **four** of this code beautiful if it contains **all four different characters**.

#### She is interested in the number of beautiful subsequences in the genetic code.

#### Formally, lets call this genetic code s of length n. Tala wants to find the number of groups of four indicies (i, j, k, l) such that **s[i] != s[j] != s[k] != s[l]** and **i < j < k < l**.

#### She asks for your help to count them.
##
### Input Format

The first line of input contains a single integer T representing the numebr of test cases 1 <= T <= 100

Each test case consists of two lines first is n the length of the genetic code (1 <= n <= 500). Follows in the next line s, a string of length n formed by using the four characters 'A', 'G', 'C' and 'T' representing the genetic code.

### Constraints

1 <= T <= 100

1 <= n <= 500

### Output Format

Print one line of output per test case an integer representing the numebr of test number of beautiful subsequences in s
##
* Sample Input 0

  3\
  6\
  AGACTT\
  5\
  AACGC\
  4\
  AGCT
* Sample Output 0

  4\
  0\
  1
* Explanation 0

  In the first test case we have four different groups of indicies i, j, k, l that fullfil the conditions:

  1- (1, 2, 4, 5) = AGCT

  2- (1, 2, 4, 6) = AGCT

  3- (2, 3, 4, 5) = GACT

  4- (2, 3, 4, 6) = GACT

  In the second test case there are 0 groups.

  In the last test case the whole string satisfies the conditions.
