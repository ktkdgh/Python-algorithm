import sys
sys.setrecursionlimit(10**8)

row, col = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
mlist = []

def dfs(x, y, temp):
    temp[x][y] = -1
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < row and 0 <= ny < col:
            if not graph[nx][ny]:
                cnt += 1
            if 0 < temp[nx][ny]:
                dfs(nx, ny, temp)
    mlist.append((x, y, cnt))
    return temp

def answer():
    years = 0
    while True:
        ice_sum = 0
        for i in graph:
            ice_sum += sum(i)
        if not ice_sum:
            return print(0)
        temp = [[b for b in a] for a in graph]
        count = 0
        for x in range(row):
            for y in range(col):
                if temp[x][y] > 0:
                    temp = dfs(x, y, temp)
                    count += 1
                if count >= 2:
                    return print(years)
        years += 1
        for x, y, cnt in mlist:
            if graph[x][y] - cnt <= 0:
                graph[x][y] = 0
            else:
                graph[x][y] -= cnt
        mlist.clear()
answer()