import itertools
import sys

N, M = map(int, sys.stdin.readline().split())
X = list(map(int, sys.stdin.readline().split()))

nPr = itertools.permutations(X, 3)
ans = 0
for i in nPr:
    if( M + 1  > sum(i)):
        ans = max(ans, sum(i))
print(ans)

