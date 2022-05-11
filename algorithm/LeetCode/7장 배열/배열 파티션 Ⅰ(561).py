# 정답

nums = [6,2,6,5,1,2]

class Solution:
    def rrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(len(nums)):
            if i % 2:
                sum += min(nums[i], nums[i-1])
        return sum

        # 파이썬 다운 방식
        # return sum(sorted(nums)[::2])
print(Solution.rrayPairSum(0, nums))