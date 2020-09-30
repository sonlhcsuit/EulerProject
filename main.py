from math import *
def triangular_num(n):
    return int((n*(n+1))/2)


def simple_sieve(n):
    sieve_of_eratosthenes = [True] * (n + 1)
    sieve_of_eratosthenes[0] = False
    sieve_of_eratosthenes[1] = False

    for i in range(2, ceil(sqrt(n)) + 1):
        if sieve_of_eratosthenes[i] == 1:
            j = i ** 2
            while j <= n:
                if (sieve_of_eratosthenes[j] == 1):
                    sieve_of_eratosthenes[j] = False
                j = j + i
    temp = [index for index, value in enumerate(sieve_of_eratosthenes) if value]
    return temp


def segment_sieve(n):
    limit = ceil(sqrt(n))
    prime = simple_sieve(limit)
    low = limit
    high = limit + limit
    # print(low)
    # print(prime)
    ct = 0
    while low < n:
        # print(ct)
        if (high > n):
            high = n
        mark = [True] * (limit + 1)
        for i in range(len(prime)):
            low_limit = (low // prime[i]) * prime[i]

            if low_limit < low:
                low_limit = low_limit + prime[i]
            # chose the start with prime[i]. if prime[i] is 2 => start with lowest divisible number in segment => 32 (2) or 33(3) or 35(5(
            for j in range(low_limit, high, prime[i]):
                mark[j - low] = False

        for i in range(low, high):
            if mark[i - low]:
                prime.append(i)
        low += limit
        high += limit
        ct += 1
    return prime

global primes
primes = segment_sieve(ceil(sqrt(10e10) + 1))

def factor(n):
    # we only need n from 0 to sqrt of n.
    # if n cannot divisible for any number in primes array => it must be prime
    # print(len(primes))
    #     print(primes)
    global primes
    i = 0
    prime = primes[i]
    factors = []
    while n != 1:
        try:
            if n % prime != 0:
                i += 1
                prime = primes[i]
            else:
                n = n // prime
                factors.append(prime)
        except:
            # n is prime
            return factors + [n]
    return factors


def count_divisor(n):
    factors = factor(n)
    factors = {x:factors.count(x)+1 for x in factors}
    no_divisors = 1

    for fact in factors:
        no_divisors*=factors[fact]
    return no_divisors

def find(threshold):
    index = 1
    while True:
        if count_divisor(triangular_num(index)) > threshold:
            return triangular_num(index)
        index+=1

print(find(500))