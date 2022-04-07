import sys

n = int(input())
a = []
for i in range(1, n+1):
    A, B = map(int, sys.stdin.readline().split())
    a.append(A+B)

for i in a:
    print(i)