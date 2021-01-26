# Sum square difference
#### Problem 6

The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

![](../resources/Problem_006.01.png)

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

![](../resources/Problem_006.02.png)

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


```python
n = 100
def sum_of_square(n):
    return sum(map(lambda x: x ** 2, range(0, n + 1)))
def square_of_sum(n):
    return sum(range(0, n + 1)) ** 2
a = sum_of_square(n)
b = square_of_sum(n)
print(b - a)
```