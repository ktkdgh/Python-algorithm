import itertools
n = [int(input()) for _ in range(9)]

nPr = itertools.permutations(n, 7)

for i in nPr:
    if sum(i) == 100:
        temp = i
        break

x = sorted(temp)
for i in x:
    print(i)