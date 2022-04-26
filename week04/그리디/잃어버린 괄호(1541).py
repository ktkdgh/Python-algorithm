from distutils.command.sdist import sdist
import sys
n = list(sys.stdin.readline().strip().split('-'))
total = []

for i in n:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    total.append(cnt)
a = total[0]
for i in range(1, len(total)):
    a -= total[i]
print(a)