from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
s, x, y = map(int, sys.stdin.readline().split())
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

def bfs():
    q = deque(viurs)
    cnt = 0
    while q:
        if cnt == s:
            break
        for _ in range(len(q)):
            z, a, b = q.popleft()
            for i in range(4):
                nx, ny = a + dx[i], b + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[a][b]
                        q.append((graph[nx][ny], nx, ny))
        cnt += 1
    return print(graph[x-1][y-1])

viurs = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            viurs.append((graph[i][j], i, j))
viurs.sort()
bfs()