import heapq
import sys

n = int(sys.stdin.readline())
card = [int(sys.stdin.readline()) for _ in range(n)]
h = []

for i in card:
    heapq.heappush(h, i)

tmp = 0
while len(h) > 1:
    a = heapq.heappop(h) + heapq.heappop(h)
    tmp += a  
    heapq.heappush(h, a)
print(tmp)