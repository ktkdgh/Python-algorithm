import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)

distance = [-1] * (n+1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
dfs(start, 0)

print(max(distance))