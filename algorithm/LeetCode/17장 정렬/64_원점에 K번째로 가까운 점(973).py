# 정답
import heapq

points = [[1,3],[-2,2]]
k = 1
# √(x1 - x2)2 + (y1 - y2)2) << 유클리드 거리
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []

        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (dist, x, y))
        
        answer = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            answer.append((x, y))

        return answer
print(Solution.kClosest(0, points, k))