import sys
sys.setrecursionlimqit(10**9)

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, graph, parent):
    for i in graph[v]:
        if parent[i] == 0:
            parent[i] = v
            dfs(i, graph, parent)

dfs(1, graph, parent)

for i in range(2, n+1):
    print(parent[i])
