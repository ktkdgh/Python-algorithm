import sys
n=int(sys.stdin.readline())
s=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
min_value = sys.maxsize
visited=[False for _ in range(n)]

def dfs(start,cur,cost):
    global  s, visited, min_value
    if start == cur and visited.count(False) == 0:
        min_value = min(min_value,cost)
    for i in range(n):
        if not s[cur][i] == 0 and not visited[i]:
            visited[i] = True
            dfs(start,i,cost+s[cur][i])
            visited[i] = False
dfs(0,0,0)
print(min_value)