# https://www.acmicpc.net/problem/10974

# 정답
import itertools, sys

n = [i for i in range(1, (int(sys.stdin.readline()) + 1))]
nPr = itertools.permutations(n, len(n))

for i in nPr:
    print(*i)