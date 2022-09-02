#check if the number is prime
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#find the next prime number
def next_prime(n):
    if is_prime(n):
        return n
    else:
        n += 1
        while True:
            for i in range(2, n):
                if n % i == 0:
                    n += 1
                    break
            else:
                return n

print(next_prime(int(input())))