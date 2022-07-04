# https://www.acmicpc.net/problem/1062

#
import sys

n, k = map(int, sys.stdin.readline().split())
word = []

for i in range(n):
    word.append(sys.stdin.readline().strip())

print(word)
