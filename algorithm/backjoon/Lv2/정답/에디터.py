# https://www.acmicpc.net/problem/1406

# 정답
import sys 

string = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())

right = []

for i in range(n):
    com = sys.stdin.readline().split()
    if com[0] == "L":
        if string:
            right.append(string.pop())
    elif com[0] == "D":
        if right:
            string.append(right.pop())
    elif com[0] == "B":
        if string:
            string.pop()
    elif com[0] == "P":
        string.append(com[1])

right.reverse()
print(''.join(string + right))