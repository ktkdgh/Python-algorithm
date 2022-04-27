import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
reserve_a = a[::-1]

increase = [1 for _ in range(n)] # 증가 수열
decrease = [1 for _ in range(n)] # 감소 수열

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if reserve_a[i] > reserve_a[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

result = [0 for _ in range(n)]
for i in range(n):
    result[i] = increase[i] + decrease[n-i-1] -1
    
print(max(result))