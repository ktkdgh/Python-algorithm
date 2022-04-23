import sys

n = int(sys.stdin.readline())
l = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    l.append((s,e))
l.sort(key=lambda x:(x[1], x[0]))
cnt = 0
last = 0
for start, end in l:
    if start >= last:
        cnt += 1
        last = end
print(cnt)