# https://www.acmicpc.net/problem/9935

# 정답
import sys

string = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

stack = []
for str in string:
    stack.append(str)
    if str == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

if stack:
    print(''.join(stack))
else:
    print("FRULA")