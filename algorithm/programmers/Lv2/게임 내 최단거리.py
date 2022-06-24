# https://programmers.co.kr/learn/courses/30/lessons/1844

# 정답
from collections import deque

def solution(maps):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    n, m = len(maps), len(maps[0])
    if n == 1 and m == 1:
        return 1

    def bfs():
        queue = deque()
        queue.append((0, 0))

        while queue:
            x, y = queue.popleft()
            if x == n-1 and y == m-1:
                return maps[x][y]
            for i in range(4):
                nx, ny = dx[i] + x, dy[i] + y
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == 1 :
                        maps[nx][ny] = maps[x][y] + 1
                        queue.append((nx, ny))
        return -1

    return bfs()

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))