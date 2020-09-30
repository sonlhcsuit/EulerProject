import math
def triangular_num(n):
    return int((n*(n+1))/2)
def count_divisor(n):
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1):
        if (n % i == 0):
            # divisor

            if (n // i == i):
                cnt = cnt + 1
            else:  # Otherwise count both
                cnt = cnt + 2
    return cnt
def find(threshold):
    index = 1
    while True:
        if(count_divisor(triangular_num(index))>threshold):
            break
        index+=1
    return triangular_num(index)

ans = find(500)
print(ans)