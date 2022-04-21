import sys

n = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

def dfs(num, graph):
    graph[num] = -2
    for i in range(len(graph)):
        if num == graph[i]:
            dfs(i, graph)

dfs(k, graph)
cnt = 0
for i in range(len(graph)):
    if graph[i] != -2 and i not in graph:
        cnt += 1

print(cnt)