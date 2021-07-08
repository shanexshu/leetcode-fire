# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        if len(lists)==2:
            return self.mergeTwo(lists[0], lists[1])
        mid = len(lists)//2
        return self.mergeTwo(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))
              
    def mergeTwo(self, l1, l2):
        ans = ListNode()
        node = ans
        while l1 and l2:
            if l1.val<=l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1: node.next = l1
        if l2: node.next = l2
        return ans.next