from inspect import stack
import sys

s = sys.stdin.readline()
stack = []
tmp = 1
answer = 0

for j in range(len(s)-1):
    if s[j] == '(':
        stack.append(s[j])
        tmp *= 2
    elif s[j] == '[':
        stack.append(s[j])
        tmp *= 3
    elif s[j] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if s[j-1] == '(':
            answer += tmp
        tmp //= 2
        stack.pop()
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if s[j-1] == '[':
            answer += tmp
        tmp //= 3
        stack.pop()

if stack:
    answer = 0
print(answer)