import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())
max_n = -1e9
min_n = 1e9

def dfs(cnt, result, add, sub, mul, div):
    global max_n, min_n
    if cnt == n:
        max_n = max(max_n, result)
        min_n = min(min_n, result)
        return
    if add > 0:
        dfs(cnt+1, result + a[cnt], add -1, sub, mul, div)
    if sub > 0:
        dfs(cnt+1, result - a[cnt], add, sub -1, mul, div)
    if mul > 0:
        dfs(cnt+1, result * a[cnt], add, sub, mul -1, div)
    if div > 0:
        dfs(cnt+1, -((-result) // a[cnt]) if result < 0 else result // a[cnt], add, sub, mul, div -1)

dfs(1, a[0], add, sub, mul, div)
print(max_n)
print(min_n)