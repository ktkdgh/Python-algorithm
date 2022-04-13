from collections import deque
import sys

n, h = [], []
while True:
    a = list(map(int, sys.stdin.readline().split()))
    if not a[0]:
        break
    n.append(a.pop(0))
    h.append(a)

for i in range(len(n)):
    high = 0
    stack = deque([])
    for j in range(len(h[i])):
        while stack and h[i][stack[-1]] > h[i][j]:
            tmp = stack.pop()
            if not stack:
                width = j
            else:
                width = j - stack[-1] - 1
            high = max(high, width * h[i][tmp])
        stack.append(j)
    while stack:
        tmp = stack.pop()
        if not stack:
            width = n[i]
        else:
            width = n[i] - stack[-1] - 1
        high = max(high, width * h[i][tmp])
    print(high)    