# https://www.acmicpc.net/problem/2231

# 틀림
import sys

n = int(sys.stdin.readline())
answer = 0

for i in range(1, n+1):
    string = list(map(int, str(i)))
    number = i + sum(string)

    if n == number:
        answer = i
        break

print(answer)