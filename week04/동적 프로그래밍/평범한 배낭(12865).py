import sys

n, k = map(int, sys.stdin.readline().split())
wei = [0]
val = [0]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    wei.append(w)
    val.append(v)

for i in range(n+1):
    for j in range(k+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif wei[i] <= j:
            dp[i][j] = max(val[i] + dp[i-1][j-wei[i]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])