import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
p.sort()

time = [0] * (n+1)
for i in range(n+1):
    time[i] = sum(p[:i])

print(sum(time[1:]))