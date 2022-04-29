# 실패
import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

def dfs(x, y):
    if dp[x][y]: return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n :
            if graph[x][y] < graph[nx][ny]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))
print(answer)