# https://www.acmicpc.net/problem/11728

# 정답
import sys

a_size, b_size = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

result = sorted(a + b)

print(*result)