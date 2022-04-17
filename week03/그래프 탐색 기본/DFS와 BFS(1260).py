from collections import deque
import sys

def dfs(v, visited = []):
    visited.append(v) 
    for w in graph[v]:
        if not w in visited:
            visited = dfs(w, visited)
    return visited

def bfs(start_v):
    visited = [start_v]
    queue = deque([start_v])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return visited

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

dfs = dfs(v)
bfs = bfs(v)
print(*dfs)
print(*bfs)