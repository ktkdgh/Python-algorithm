import sys

n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]
coin.sort(reverse=True)

count = 0
for i in coin:
    if not k: break
    if i > k: continue
    count += k//i
    k %= i
print(count)