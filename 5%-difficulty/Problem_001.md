# Multiples of 3 and 5
#### Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

---

To solve this problem, we can easy to use a brute-force approach like that

```python
def multiples_3_5(n):
    _sum = 0
    for i in range(1,n//3+1):
        _sum += i*3
        _sum += 0 if i*5 >= n  else i*5
        _sum -= 0 if i*15 >= n else i*15
    return _sum
```

**Notes**
- Make sure you have cover cases which are multiples of 3 and 5 (15, 30, 45)
