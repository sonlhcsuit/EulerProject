# Largest palindrome product
#### Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

```python
def is_palindrome(num):
    # print(num)
    reversed_num = str(num)[::-1]
    # print(reversed_num,num)
    return int(reversed_num) == int(num)

def find(no_digit):
    largest = 10**no_digit - 1
    smallest = 10 **(no_digit-1)
    largest_palindrome = 0
    smallest_number = smallest
    print(largest,smallest)
    i = largest
    # if we find some palindrome at ith loop and jth loop. And it must be largest jth of J loop. ith*jth => palindrome.
    # So we only need run the I loop down to j (not necessary to down to zero )
    while i > smallest_number:
        # print(i)
        j=i
        while j > smallest_number:
            number = j * i
            if(is_palindrome(number) and number>largest_palindrome):
                largest_palindrome=number
#                 print(number)
                if(j > smallest_number):
                    smallest_number = j
                break
            j=j-1
        i= i -1
    return largest_palindrome
    
# import time
# start =time.time()
# a = find(3)
# end = time.time()
# print(end-start)
# print(a)
```
