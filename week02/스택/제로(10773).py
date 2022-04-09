import sys

k = int(sys.stdin.readline())
n = [int(sys.stdin.readline()) for _ in range(k)]

stack = []
for i in n:
    if i != 0:
        stack.append(i)
    else:
        stack.pop()

print(sum(stack))
