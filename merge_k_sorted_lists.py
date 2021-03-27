# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        def merge(l1, l2):
            if not l1: return l2
            if not l2: return l1
            if l1.val > l2.val:
                return merge(l2, l1)
            # l1 has lesser first val
            ret = ListNode(l1.val)
            ret.next = merge(l1.next, l2)
            return ret
            
        if not lists: return None
        if len(lists)<2: return lists[0]
        if len(lists)==2:
            h1 = lists[0]
            h2 = lists[1]
            # merge the two lists
            return merge(h1, h2)
        
        mid = len(lists)//2
        return merge(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))
    
    