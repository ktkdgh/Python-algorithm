import sys

def dfs(start, group):
    global flag
    if flag:
        return
    visited[start] = group
    for i in graph[start]:
        if not visited[i]:
            dfs(i, -group)
        elif visited[start] == visited[i]:
            flag = True
            return

for _ in range(int(sys.stdin.readline())):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    flag = False

    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, v+1):
        if not visited[i]:
            dfs(i, 1)
            if flag:
                break
    if flag:
        print("NO")
    else:
        print("YES")