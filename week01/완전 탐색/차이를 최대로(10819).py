import itertools
import sys
n = int(input())
x = map(int, sys.stdin.readline().split())

nPr = itertools.permutations(x, n)

y = []

for i in nPr:
    temp = 0
    for j in range(n - 1):
        temp += abs(i[j] - i[j+1])
    y.append(temp)

print(max(y))