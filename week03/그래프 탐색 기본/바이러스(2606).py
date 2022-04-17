import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

def dfs(v, visited = []):
    visited.append(v) 
    for w in graph[v]:
        if not w in visited:
            visited = dfs(w, visited)
    return visited

answer = dfs(1)
print(len(answer[1:]))
