import heapq
import sys

n = int(sys.stdin.readline())
x = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d = int(sys.stdin.readline())

roads = []
for i in x:
    if abs(i[0] - i[1]) <= d:
        roads.append(sorted(i))
roads.sort(key=lambda x:x[1])

answer = 0
heap = []
for i in roads:
    if not heap:
        heapq.heappush(heap, i)
    else:
        while heap[0][0] < i[1] - d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, i)
    answer = max(answer, len(heap))
print(answer)