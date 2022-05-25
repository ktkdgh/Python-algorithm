# 정답
import itertools

n = 2
k = 1

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        if n <= 1:
            return [[n]]
        nums = [i for i in range(1, n+1)]
        return list(itertools.combinations(nums, k))

print(Solution.combine(0, n, k))