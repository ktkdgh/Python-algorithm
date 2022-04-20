from collections import deque
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
cost = [[0 for _ in range(n+1)] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    graph[y].append((x, k))
    indegree[x] += 1

def topology_sort():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for node, c in graph[now]:
            if cost[now].count(0) == n + 1:
                cost[node][now] += c
            else:
                for i in range(1, n+1):
                    cost[node][i] += cost[now][i] * c
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(node)

topology_sort()

for idx, c in enumerate(cost[n]):
    if c != 0:
        print(idx, c)