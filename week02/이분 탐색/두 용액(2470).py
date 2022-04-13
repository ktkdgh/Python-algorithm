import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
x.sort()
min = 2000000000

for i in range(n - 1):
    start = i + 1
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        temp = x[i] + x[mid]
        if abs(temp) < min:
            min = abs(temp)
            a, b = i, mid
        if temp < 0:
            start = mid + 1
        else:
            end = mid - 1
print(x[a], x[b])