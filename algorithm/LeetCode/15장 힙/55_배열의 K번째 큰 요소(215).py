# 정답
import heapq

nums = [3,2,1,5,6,4]
k = 2
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, -num)
        for _ in range(k-1):
            heapq.heappop(heap)
        return -heapq.heappop(heap)

print(Solution.findKthLargest(0, nums, k))