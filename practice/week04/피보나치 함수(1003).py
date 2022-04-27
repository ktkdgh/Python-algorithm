import sys

def fibo(n):
    if len(one) <= n:
        for i in range(3, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    return zero[n], one[n]

answer = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    zero = [1, 0, 1]
    one = [0, 1, 1]
    fibo(n)
    answer.append((zero[n], one[n]))

for i in answer:
    print(*i)