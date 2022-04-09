import sys

n, k = map(int, sys.stdin.readline().split())
revel = [int(sys.stdin.readline()) for _ in range(n)]

start = min(revel)
end = max(revel) 

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in revel:
        if i < mid:
            total += mid - i
    if total > k:
        end = mid -1
    else:
        result = mid
        start = mid + 1
        
print(result)