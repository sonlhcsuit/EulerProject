# Largest prime factor
#### Problems 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

We can use segment of sieve of Eratosthenes algorithm
```python
from math import *
def simple_sieve(n):
    sieve_of_eratosthenes = [True]*(n+1)
    sieve_of_eratosthenes[0] = False
    sieve_of_eratosthenes[1] = False

    for i in range(2,ceil(sqrt(n))+1):
        if sieve_of_eratosthenes[i] == 1:
            j = i**2
            while j <= n:
                if(sieve_of_eratosthenes[j]==1):
                    sieve_of_eratosthenes[j] = False
                j=j+i
    temp = [index for index,value in enumerate(sieve_of_eratosthenes) if value]
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
        if(high>n):
            high = n
        mark = [True]*(limit+1)
        for i in range(len(prime)):
            low_limit = (low // prime[i])*prime[i]

            if low_limit < low :
                low_limit = low_limit+prime[i]
            # chose the start with prime[i]. if prime[i] is 2 => start with lowest divisible number in segment => 32 (2) or 33(3) or 35(5(
            for j in range(low_limit,high,prime[i]):
                mark[j-low] = False

        for i in range(low,high):
            if mark[i-low]:
                prime.append(i)
        low += limit
        high+= limit
        ct+=1
    return prime

def factor(n):
    # we only need n from 0 to sqrt of n.
    # if n cannot divisible for any number in primes array => it must be prime
    primes = segment_sieve(ceil(sqrt(n)+1))
    # print(len(primes))
#     print(primes)
    i=0
    prime = primes[i]
    factors = []
    while n != 1:
        try:
            if n % prime != 0:
                i+=1
                prime = primes[i]
            else:
                n = n//prime
                factors.append(prime)
        except:
            return factors+[n]
    return factors

# n = 600851475143
# n=9
# temp  = factor(n)
# print(temp[-1])
```
In order to speed up, we use a segment sieve.
