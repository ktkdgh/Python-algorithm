from collections import deque
import sys
n = int(sys.stdin.readline())
x = [list(sys.stdin.readline().split()) for _ in range(n)]

q = deque([])
for i in x:
    if i[0] == 'push':
        q.append(i[1])
    elif i[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif i[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
    elif i[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif i[0] == 'size':
        print(len(q))
    else:
        if not q:
            print(1)
        else:
            print(0)