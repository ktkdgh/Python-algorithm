import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
mlist = []
