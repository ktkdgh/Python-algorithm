# https://www.acmicpc.net/problem/1269

# 정답
import sys

a_length, b_length = map(int, sys.stdin.readline().split())
a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))

print(len(a-b) + len(b-a))