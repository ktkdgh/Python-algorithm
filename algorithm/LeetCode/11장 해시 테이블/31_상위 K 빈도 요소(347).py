# 정답
import collections

nums = [1,1,1,2,2,3,3,2,1,3,22,1,2,3]
k = 2

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = collections.Counter(nums).most_common(k)
        answer = []
        for i in range(k):
            answer.append(count[i][0])
        return answer
        
print(Solution.topKFrequent(0, nums, k))