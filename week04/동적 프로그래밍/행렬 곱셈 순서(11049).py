import sys

n = int(sys.stdin.readline())

hang = []
for _ in range(n):
    r, c = map(int, sys.stdin.readline().split())
    hang.append((r, c))

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

