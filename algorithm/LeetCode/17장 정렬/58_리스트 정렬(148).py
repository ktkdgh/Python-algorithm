# 정답
from typing import Optional

head = [4,2,1,3]
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        stack = []

        while tmp:
            stack.append(tmp.val)
            tmp = tmp.next
        
        stack.sort()
        tmp = head
        for i in range(len(stack)):
            tmp.val = stack[i]
            tmp = tmp.next
        
        return head