# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        if l2.val<l1.val:
            return self.mergeTwoLists(l2, l1)
        
        next1 = l1.next 
        l1.next = self.mergeTwoLists(next1, l2)
        return l1