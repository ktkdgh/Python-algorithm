from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if nx < 0 or ny < 0 or ny >= m or nx >= n:
                continue
            elif graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[a][b] + 1
    return graph[-1][-1]
print(bfs(0,0))