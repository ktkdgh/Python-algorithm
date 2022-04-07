import sys

avg = []
n = int(input())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    total = 0
    for j in range(len(a[i])):
        if j > 0:
            total = total + a[i][j]
    avg.append(int(total/a[i][0]))

for i in range(n):
    cnt = 0
    for j in range(len(a[i])):
        if j > 0 and avg[i] < a[i][j] :
            cnt += 1
    print('%.3f%%' % (float(cnt/a[i][0] * 100)))
    