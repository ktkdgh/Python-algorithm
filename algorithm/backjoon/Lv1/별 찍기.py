# https://www.acmicpc.net/problem/2447

# 틀림
import sys

n = int(sys.stdin.readline())

def star(n):
    if n == 1:
        return ["*"]
    
    stars = star(n//3)
    L = []

    for i in stars:
        L.append(i * 3)
    for i in stars:
        L.append(i + ' ' * (n//3) + i)
    for i in stars:
        L.append(i * 3)
    return L

print('\n'.join(star(n)))