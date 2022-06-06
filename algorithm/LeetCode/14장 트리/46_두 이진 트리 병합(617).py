# 정답
from asyncio.windows_events import NULL
from typing import Optional

root1 = [1,3,2,5] 
root2 = [2,1,3,NULL,4,NULL,7]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
        
            return node
        else:
            return root1 or root2

print(Solution.mergeTrees(0, root1, root2))