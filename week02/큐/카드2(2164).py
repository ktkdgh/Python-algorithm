from collections import deque
import sys
n = int(sys.stdin.readline())

q = deque([i for i in range(1, n+1)])
while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
print(*q)