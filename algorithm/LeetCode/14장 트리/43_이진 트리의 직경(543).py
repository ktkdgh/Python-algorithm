import collections
from typing import Optional
root = [1,2,3,4,5]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = collections.deque(root)

        def dfs(start):
            curr = queue.popleft()
            

        
            

print(Solution.diameterOfBinaryTree(0, root))