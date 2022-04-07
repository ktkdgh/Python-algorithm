import sys
A, B = map(int, sys.stdin.readline().split())

x = list(str(A))
y = list(str(B))
a = ''
b = ''
for i in range(2, -1, -1):
    a = a + x[i]
    b = b + y[i]

if a > b:
    print(a)
else:
    print(b)