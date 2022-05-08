# 성공
nums = [3, 3]
target = 6

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 책 풀이 74ms
        # nums_map = {}
        # for i, num in enumerate(nums):
        #     nums_map[num] = i

        # for i, num in enumerate(nums):
        #     if target - num in nums_map and i != nums_map[target- num]:
        #         return [i, nums_map[target - num]]
        
        # 내 풀이 3874ms
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]



print(Solution.twoSum(0, nums, target))
