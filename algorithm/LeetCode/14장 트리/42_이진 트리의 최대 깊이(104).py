# 정답
import collections
from typing import Optional

root = [3,9,20,0,0,15,7]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        depth = 0
        if root is None:
            return depth

        while queue:
            depth += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return depth

print(Solution.maxDepth(0, root))