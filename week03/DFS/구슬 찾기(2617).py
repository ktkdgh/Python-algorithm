import sys

n, m = map(int, sys.stdin.readline().split())
graph_a = [[] for _ in range(n+1)]
graph_b = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph_a[u].append(v)
    graph_b[v].append(u)

def dfs(start, graph, visited):
    for i in graph[start]:
        if not i in visited:
            visited.append(i)
            dfs(i, graph, visited)
    return visited

answer = 0
for i in range(1, n+1):
    answer_a, answer_b = dfs(i, graph_a, []), dfs(i, graph_b, [])
    if len(answer_a) >= (n+1)//2:
        answer += 1
    elif len(answer_b) >= (n+1)//2:
        answer += 1
print(answer)