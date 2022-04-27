import sys

n, m = map(int, sys.stdin.readline().split())
stone = [int(sys.stdin.readline()) for _ in range(m)]
INF = int(1e9)

dp = [[INF] * (int((2*n)**0.5)+2) for _ in range(n+1)]
dp[1][0] = 0

for i in range(2, n+1):
    if i in stone:
        continue
    for v in range(1, int((2*i)**0.5) +1):
        dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1]) + 1

answer = min(dp[n])
if answer == INF:
    print(-1)
else:
    print(answer)
