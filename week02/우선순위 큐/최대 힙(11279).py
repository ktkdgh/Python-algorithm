import sys
import heapq

n = int(sys.stdin.readline())
x = [int(sys.stdin.readline()) for _ in range(n)]
heap = []
for i in x:
    if i == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -i)