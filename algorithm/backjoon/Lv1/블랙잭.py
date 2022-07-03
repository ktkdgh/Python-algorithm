# https://www.acmicpc.net/problem/2798

# 정답
import itertools, sys

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

nPr = itertools.permutations(card, 3)
card_max = 0

for c in nPr:
    if m >= sum(c):
        card_max = max(card_max, sum(c))

print(card_max)