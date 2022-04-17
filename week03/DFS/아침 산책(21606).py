import sys
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
a = list(map(int, list("0" + sys.stdin.readline().strip())))
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

tmp = 0
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    if a[u] == 1 and a[v] == 1:
        tmp += 2

def dfs(start, cnt):
    visited[start] = 1
    for i in graph[start]:
        if a[i] == 1:
            cnt += 1
        elif a[i] == 0 and visited[i] == 0:
            cnt = dfs(i, cnt)
    return cnt

for i in range(1, n+1):
    if a[i] == 0 and visited[i] == 0:
        x = dfs(i, 0)
        tmp += x * (x-1)
print(tmp)