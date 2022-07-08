# 정답
nums = [-1,0,3,5,9,12]
target = 9
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) -1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        else:
            return -1
        

print(Solution.search(0, nums, target))