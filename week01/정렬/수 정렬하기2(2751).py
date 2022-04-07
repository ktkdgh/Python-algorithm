import sys
n = int(sys.stdin.readline())
y = [int(int(sys.stdin.readline())) for _ in range(n)]
x = sorted(y)
for i in x:
    print(i)