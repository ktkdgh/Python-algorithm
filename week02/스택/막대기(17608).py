import sys
n = int(sys.stdin.readline())
stack = [int(sys.stdin.readline()) for _ in range(n)]
cnt = 1
max = stack[-1]
for i in range(len(stack)-1, -1, -1):
    if stack[i] > max:
        cnt += 1
        max = stack[i]
print(cnt)