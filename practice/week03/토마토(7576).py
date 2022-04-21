from collections import deque
import sys

col, row = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque([])

for i in range(row):
    for j in range(col):
        if graph[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
bfs()
answer = 0
for i in graph:
    for j in i:
        if not j:
            print(-1)
            exit(0)
    answer = max(answer, max(i))
print(answer - 1)