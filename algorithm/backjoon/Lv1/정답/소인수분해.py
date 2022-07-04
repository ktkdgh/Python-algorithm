# https://www.acmicpc.net/problem/11653

# 정답
import sys

n = int(sys.stdin.readline())
m = 2

while n != 1:
    div, mod = divmod(n, m)
    if mod == 0:
        print(m)
        n = div
    else:
        m += 1