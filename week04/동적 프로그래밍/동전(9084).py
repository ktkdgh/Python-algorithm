import sys

answer = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    coin = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    d = [0] * (m + 1) 
    d[0] = 1

    for i in coin:
        for j in range(m + 1):
            if j >= i:
                d[j] += d[j - i]
    answer.append(d[m])

for i in answer:
    print(i)