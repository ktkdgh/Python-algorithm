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
    if a[u] and a[v]:
        tmp += 2

def dfs(start, cnt):
    visited[start] = 1
    for i in graph[start]:
        if a[i]:
            cnt += 1
        elif not a[i] and not visited[i]:
            cnt = dfs(i, cnt)
    return cnt

for i in range(1, n+1):
    if not a[i] and not visited[i]:
        x = dfs(i, 0)
        tmp += x * (x-1)
print(tmp)