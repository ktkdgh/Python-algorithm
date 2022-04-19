from collections import deque
import sys

r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(r)]
water_graph = [[0 for _ in range(c)] for _ in range(r)]
move_graph = [[0 for _ in range(c)] for _ in range(r)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()
water = deque()

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            queue.append((i, j))
            graph[i][j] = '.'
        elif graph[i][j] == '*':
            water.append((i, j))
        elif graph[i][j] == 'D':
            left, right = i, j

def bfs():
    while water:
        a, b = water.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == '.' and water_graph[nx][ny] == 0:
                    water_graph[nx][ny] = water_graph[a][b] + 1
                    water.append((nx, ny))
    while queue:
        x, y = queue.popleft()
        for j in range(4):
            nx_q, ny_q = x + dx[j], y + dy[j]
            if 0 <= nx_q < r and 0 <= ny_q < c:
                if graph[nx_q][ny_q] in ".D" and move_graph[nx_q][ny_q] == 0 and (move_graph[x][y] + 1 < water_graph[nx_q][ny_q] or water_graph[nx_q][ny_q] == 0):
                    move_graph[nx_q][ny_q] = move_graph[x][y] + 1
                    queue.append((nx_q, ny_q))

bfs()
if move_graph[left][right]:
    print(move_graph[left][right])
else:
    print("KAKTUS")