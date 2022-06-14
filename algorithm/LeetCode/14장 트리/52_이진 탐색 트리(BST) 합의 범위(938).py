# 실패
from typing import Optional

root = [10,5,15,3,7,0,18]
low = 7 
high = 15
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    result = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        return (root.val if low <= root.val <= high else 0) + \
                self.rangeSumBST(root.left, low, high) + \
                self.rangeSumBST(root.right, low, high)

print(Solution.rangeSumBST(0, root, low, high))