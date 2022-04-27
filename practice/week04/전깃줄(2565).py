import sys

n = int(sys.stdin.readline())
cord = []
cord_b = []
for _ in range(n):
    cord.append(list(map(int, sys.stdin.readline().split())))
cord.sort(key=lambda x:x[0])

for i in range(n):
    cord_b.append(cord[i][1])

dp = [1] * (n+1)

for i in range(n):
    for j in range(i):
        if cord_b[i] > cord_b[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))