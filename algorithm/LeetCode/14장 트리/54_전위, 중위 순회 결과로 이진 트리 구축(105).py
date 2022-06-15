# 정답
from typing import Optional

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if inorder:
            index = inorder.index(preorder.pop(0))

            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index + 1:])

            return root

print(Solution.buildTree(0, preorder, inorder))