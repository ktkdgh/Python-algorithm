import sys

m, n, l = map(int, sys.stdin.readline().split())
m_location = list(map(int, sys.stdin.readline().split()))
animal = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

animal.sort()
