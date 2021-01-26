# Summation of primes
#### Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

---
We can reuse *segment_sieve* function from Problem_003

```python
primes = segment_sieve(int(2e6))
print(sum(primes))
```