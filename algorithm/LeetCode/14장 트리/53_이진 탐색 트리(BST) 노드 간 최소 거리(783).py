# 정답
from typing import Optional

root = [4,2,6,1,3]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    result = 1000000
    prev = -1000000
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result
print(Solution.minDiffInBST(0, root))