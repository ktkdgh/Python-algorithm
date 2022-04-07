import sys

w, h = map(int, sys.stdin.readline().split())

wArr = [0, w]
hArr = [0, h]

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    if a == 0:
        hArr.append(b)
    else:
        wArr.append(b)
wArr.sort()
hArr.sort()

a = []
b = []

for i in range(len(wArr)-1):
    a.append(abs(wArr[i] - wArr[i + 1]))

for i in range(len(hArr)-1):
    b.append(abs(hArr[i] - hArr[i + 1]))
print(max(a) * max(b))