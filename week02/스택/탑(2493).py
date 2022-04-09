import sys

n = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
stack = []
a = [0] * n
for i in range(n):
    while stack and top[stack[-1]] < top[i]:
        stack.pop()
    if stack:
        a[i] = stack[-1] + 1
    stack.append(i)
    
for i in range(len(a)):
    print(a[i], end=' ')