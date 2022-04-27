import sys

n = int(sys.stdin.readline())
three = []
for _ in range(n):
    three.append(list(map(int, sys.stdin.readline().split())))
k = 2
for i in range(1, n):
    for j in range(k):
        if j == 0:
            three[i][j] += three[i-1][j]
        elif i == j:
            three[i][j] += three[i-1][j-1]
        else:
            three[i][j] += max(three[i-1][j-1], three[i-1][j])
    k += 1
print(max(three[-1]))