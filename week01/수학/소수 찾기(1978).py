import sys
import math

def is_prime_num(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False
    
    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2
            while (i * j) <= n:
                arr[i*j] = False
                j += 1
    return arr

n = int(input())
x = list(map(int, sys.stdin.readline().split()))

max = 0
for i in x:
    if max < i :
        max = i
arr = is_prime_num(max)
cnt = 0

for i in range(len(arr)):
    for j in range(len(x)):
        if arr[i] == True and i == x[j]:
            cnt += 1
print(cnt)