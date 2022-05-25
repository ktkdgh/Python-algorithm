# 정답
from itertools import permutations
nums = [1,2,3]

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return list(permutations(nums, len(nums)))

print(Solution.permute(0, nums))