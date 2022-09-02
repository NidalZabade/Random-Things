import itertools
flatten_iter = itertools.chain.from_iterable

#find if the number is prime or not
def is_prime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

#find the divisors of the number
def factors(n):
    return set(flatten_iter((i, n//i) 
                for i in range(1, int(n**0.5)+1) if n % i == 0))
#find all distinct prime factorization of the number
def find_prime_factorization(n):
    prime_factorization = []
    while n != 1:
        for x in range(2, n + 1):
            if is_prime(x) and n % x == 0:
                prime_factorization.append(x)
                n = n // x
                break
    return prime_factorization
n=int(input())
if is_prime(n):
    print("YES")
    print(n)
    L=sorted(factors(n))
    print(*L,sep=' ')
else:
    print("NO")
    L=sorted(factors(n))
    list=list(dict.fromkeys(find_prime_factorization(n)))
    print(*list,sep=' ')
    print(*L,sep=' ')
    