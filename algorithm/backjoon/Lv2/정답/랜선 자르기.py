# https://www.acmicpc.net/problem/1654

# 정답
import sys

k, n = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]
lan.sort()

start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in lan:
        cnt += i // mid 
    
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)