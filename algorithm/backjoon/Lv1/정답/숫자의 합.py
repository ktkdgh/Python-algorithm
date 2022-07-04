# https://www.acmicpc.net/problem/11720

# 정답
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().strip()))

print(sum(num))