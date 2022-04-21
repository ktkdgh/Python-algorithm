# 성공
import sys
INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = []
for a in range(1, n + 1):
    temp = 0
    for b in range(1, n + 1):
        if graph[a][b] != INF:
            temp += graph[a][b]
    answer.append((a, temp))
answer.sort(key=lambda x:x[1])
print(answer[0][0])