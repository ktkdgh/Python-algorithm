# 성공
import sys

n = int(sys.stdin.readline())
graph = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
cnt = 0

def dfs(x, y):
    global cnt 
    visited[x][y] = 1
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx, ny)
answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            dfs(i, j)
            answer.append(cnt)
            cnt = 0
answer.sort()
print(len(answer))
for i in answer:
    print(i)