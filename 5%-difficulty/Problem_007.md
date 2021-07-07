# 10001st prime
#### Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

---
NOTES: I reused "simple_sieve" and "segmen_sieve" function from Problem_003
```python
primes = segment_sieve(int(1e6))
print(primes[10001-1])
```