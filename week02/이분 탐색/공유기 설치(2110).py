import sys

n, c = map(int, sys.stdin.readline().split())
x = [int(sys.stdin.readline()) for _ in range(n)]
x.sort()

start = 1
end = x[-1] - x[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    current = x[0]
    count = 1

    for i in range(1, len(x)):
        if x[i] >= current + mid:
            count += 1
            current = x[i]
        
    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid -1
print(answer)