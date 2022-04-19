from collections import deque
import sys

col, row, hight = map(int, sys.stdin.readline().split())
graph = [[[tomato for tomato in list(map(int, sys.stdin.readline().split()))] for _ in range(row)] for _ in range(hight)]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]
queue = deque()

for i in range(hight):
    for j in range(row):
        for k in range(col):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))
def bfs():
    while queue:
        h, x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nh = h + dh[i]
            if 0 <= nx < row and 0 <= ny < col:
                if nh < 0 or nh >= hight:
                    continue
                if graph[nh][nx][ny] == 0:
                    graph[nh][nx][ny] = graph[h][x][y] + 1
                    queue.append((nh, nx, ny))

bfs()
answer = 0
for i in graph:
    for j in i:
        for k in j:
            if not k:
                print(-1)
                exit(0)
        answer = max(answer, max(j))
print(answer - 1)