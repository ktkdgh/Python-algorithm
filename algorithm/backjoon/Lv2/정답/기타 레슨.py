# https://www.acmicpc.net/problem/2343

# 정답
import sys

n, m = map(int, sys.stdin.readline().split())
video = list(map(int, sys.stdin.readline().split()))

start = max(video)
end = sum(video)

while start <= end:
    mid = (start + end) // 2
    answer = 0
    cnt = 1

    for v in video:
        if answer + v > mid:
            cnt += 1
            answer = 0
        answer += v

    if cnt <= m:
        end = mid - 1
    else:
        start = mid + 1

print(start)
