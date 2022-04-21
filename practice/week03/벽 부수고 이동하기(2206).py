from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0, 0))

    while q:
        a, b, c = q.popleft()
        if a == n -1 and b == m - 1: return print(visited[a][b][c])
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and c == 0:
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    q.append((nx, ny, 1))
                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    q.append((nx, ny, c))
    return print(-1)
bfs()