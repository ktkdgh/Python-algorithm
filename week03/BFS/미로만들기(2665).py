import heapq
import sys

n = int(sys.stdin.readline())
graph = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue = []
    heapq.heappush(queue, (0, x, y))
    while queue:
        cnt, a, b = heapq.heappop(queue)
        if a == n - 1  and  b == n - 1: return cnt
        if visited[a][b] == 1: continue
        visited[a][b] = 1
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    heapq.heappush(queue, (cnt + 1, nx, ny))
                else: 
                    heapq.heappush(queue, (cnt, nx, ny))
print(bfs(0,0))