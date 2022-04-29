# 실패
import heapq, sys

n, k = map(int, sys.stdin.readline().split())
bo = []
for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(bo, (m, v))
bag = [int(sys.stdin.readline()) for _ in range(k)]
bag.sort()

result = 0
answer = []
for i in bag:
    while bo and i >= bo[0][0]:
        wei, val = heapq.heappop(bo)
        heapq.heappush(answer, -val)
    if answer:
        result += -heapq.heappop(answer)
print(result)