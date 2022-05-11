# 정답
nums = [-1,1,0,-3,3]

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = []
        temp = 1
        for i in range(len(nums)):
            answer.append(temp)
            temp *= nums[i]
        
        temp = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= temp
            temp *= nums[i]
        return answer

print(Solution.productExceptSelf(0, nums))