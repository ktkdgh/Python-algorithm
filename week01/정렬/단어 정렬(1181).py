import sys
n = int(sys.stdin.readline())
y = [sys.stdin.readline().strip() for _ in range(n)]
z = list(set(y))
list.sort(z, key=lambda x :(len(x), x))
for i in z:
    print(i)
