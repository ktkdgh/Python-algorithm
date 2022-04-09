import sys

def bin_search(a, key):
    pl = 0
    pr = len(a) -1

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return 1
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return 0

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
a.sort()

c = []
for i in b:
    c.append(bin_search(a, i))

for i in c:
    print(i)