import sys

answer = []
for _ in range(int(sys.stdin.readline())):
    days = int(sys.stdin.readline())
    dream = list(map(int, sys.stdin.readline().split()))

    value = 0
    max = 0
    for i in range(len(dream)-1, -1, -1):
        if dream[i] > max:
            max = dream[i]
        else:
            value += max - dream[i]
    answer.append(value)

print(*answer, sep='\n')