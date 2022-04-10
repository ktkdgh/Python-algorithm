import heapq
import sys

n = int(sys.stdin.readline())
x = [int(sys.stdin.readline()) for _ in range(n)]

min_heap = []
max_heap = []

for i in x:
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, -i)
    else:
        heapq.heappush(min_heap, i)

    if min_heap and min_heap[0] < -max_heap[0]:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    
    print(-max_heap[0])