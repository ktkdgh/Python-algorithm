import sys

answer = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    test = [0] * (n+1)
    for _ in range(n):
        paper, interview = map(int, sys.stdin.readline().split())
        test[paper] = interview
    
    max_test = test[1]
    cnt = 1
    for i in range(2, n+1):
        if max_test > test[i]:
            max_test = test[i]
            cnt += 1
    answer.append(cnt)

for i in answer:
    print(i)    