import sys

def dfs(depth):
    if depth == k:
        s.add(''.join(map(str, li)))
        return
    for i in range(n):
        if check[i]:
            continue
        li.append(card[i])
        check[i] = 1
        dfs(depth + 1)
        li.pop()
        check[i] = 0

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
card = [int(sys.stdin.readline()) for _ in range(n)]

li, s = [], set()
check = [0] * n
dfs(0)
print(len(s))