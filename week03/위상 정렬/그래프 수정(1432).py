import heapq
import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
result = [0] * (n+1)

for i in range(1, n+1):
    temp = [0] + list(map(int, sys.stdin.readline().strip()))
    for j in range(1, n+1):
        if temp[j] == 1:
            graph[j].append(i)
            indegree[i] += 1

def topology_sort():
    q = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(q, -i)
    r = n
    while q:
        now = -heapq.heappop(q)
        result[now] = r

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, -i)
        r -= 1
    
topology_sort()

if result.count(0) > 1:
    print(-1)
else:
    print(*result[1:])