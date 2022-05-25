# 정답
nums = [1,2,3]

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def dfs(index, path):
            result.append(path)
            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])

        dfs(0, [])
        return result

print(Solution.subsets(0, nums))