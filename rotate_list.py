# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # make the last node point to first
        # make the next to last node point to None
        if not head: return
        n = 0
        node = head
        revlist = None
        while node:
            n += 1
            tail = node
            node = node.next
        simpk = k % n
        if simpk == 0: return head
        
        node = head
        for _ in range(n-simpk):
            tail.next = head
            tail = head
            nexthead = head.next
            head.next = None
            head = nexthead
            
        return head