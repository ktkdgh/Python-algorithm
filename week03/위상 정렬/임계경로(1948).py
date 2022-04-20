from collections import deque
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
graph_rev = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    x, y, t = map(int, sys.stdin.readline().split())
    graph[x].append((y,t))
    graph_rev[y].append((x, t))
    indegree[y] += 1

start, end = map(int, sys.stdin.readline().split())

def topology_sort():
    q = deque()
    time_graph = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append((i, 0))

    while q:
        now, ntime = q.popleft()
        for node, time in graph[now]:
            indegree[node] -= 1
            time_graph[node] = max(time_graph[node], time + time_graph[now])
            if indegree[node] == 0:
                q.append((node, ntime + time))
    
    return time_graph

time = topology_sort()
edges = set()
def bfs():
    q = deque()
    q.append((end, 0))

    while q:
        now, ntime = q.popleft()
        for node, times in graph_rev[now]:
            if time[now] == times + time[node] and (node, now) not in edges:
                edges.add((node, now))
                q.append((node, times + ntime))
bfs()

print(time[end])
print(len(edges))