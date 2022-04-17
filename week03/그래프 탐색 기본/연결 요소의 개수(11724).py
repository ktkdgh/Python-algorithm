import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n + 1)

for i in range(1, n+1):
    parent[i] = i

edges = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))
edges.sort()

for edge in edges:
    u, v = edge
    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent, u, v)

result = []
for i in parent:
    result.append(find_parent(parent, i))

print(len(set(result[1:])))