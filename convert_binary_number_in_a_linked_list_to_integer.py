# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        stack = []
        node = head
        ans = 0
        k = 0
        while node:
            stack.append(node.val)
            node = node.next
        while stack:
            ans += stack.pop() * 2**k
            k += 1
            
        return ans