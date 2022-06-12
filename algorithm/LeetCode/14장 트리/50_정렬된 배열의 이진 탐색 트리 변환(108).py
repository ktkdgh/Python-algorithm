# 정답
from typing import Optional

nums = [-10,-3,0,5,9]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def sortToBST(nums):
            if len(nums) == 0:
                return None

            mid = nums[len(nums) // 2]
            root = TreeNode(mid)
            root.left = sortToBST(nums[:len(nums) // 2])
            root.right = sortToBST(nums[len(nums) // 2 + 1:])
            return root
        return sortToBST(nums)

print(Solution.sortedArrayToBST(0, nums))