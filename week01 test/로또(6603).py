# 실패
import sys
k, s = [], []
def dfs(cnt, n, k, s):
    if cnt == 6:
        print(*lotto)
        return
    for i in range(n, k):
        lotto.append(s[i])
        dfs(cnt + 1, i + 1, k, s)
        lotto.pop()

while True:
    num = list(map(int, sys.stdin.readline().split()))
    if num[0] == 0:
        break  
    k.append(num.pop(0))
    s.append(num)
print(k, s)

for i in range(len(k)):
    lotto = []
    dfs(0, 0, k[i], s[i])
    if i < len(k) -1:
        print()