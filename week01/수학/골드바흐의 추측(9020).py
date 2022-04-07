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
x = [int(input()) for _ in range(n)]
y = []
max = 0
for i in x:
    if max < i :
        max = i
arr = is_prime_num(max)

for i in x:
    a, b = i//2, i//2
    while a > 0:
        if arr[a] and arr[b]:
            print(a, b)
            break;
        else:
            a -= 1
            b += 1


