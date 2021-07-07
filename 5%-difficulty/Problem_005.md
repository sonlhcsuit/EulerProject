# Smallest multiple
#### Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

First of all, it must be evenly divisible by all prime numbers from 2 to 20.

After that, you can factor all numbers from 2 to 20 add some potential prime number to divisors-list

---

Note: I reused some function such as simple_sieve to calculate prime numbers 
```python
def counting(input_seq):
    cts = []
    value = input_seq[0]
    ct = 0
    for element in input_seq:
        if (value == element):
            ct += 1
        else:
            cts.append([value, ct])
            value = element
            ct = 1
    cts.append([value, ct])
    return cts


def find(n):
    prod = 1
    lof = {}
    divisor = [[x, 1] for x in simple_sieve(n)]
    for num in divisor:
        lof[str(num[0])] = num[1]
    for i in range(2, n + 1):
        factors = counting(factor(i))
        for number, amount in factors:
            if (lof[str(number)] < amount):
                lof[str(number)] = amount
    return lof
    for key in lof:
        value = int(key)
        times = int(lof[key])
        actual = value**times
        prod = prod*actual
        # print(prod)

    return prod

n = 20
print(find(n))
```
