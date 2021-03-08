# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        odd = ListNode(-1)
        odd.next = head
        even = ListNode(-1)
        if head:
            even.next = head.next
        node = head
        count = 0
        while node and node.next:
            count += 1
            nextnode = node.next
            node.next = node.next.next
            if not nextnode.next and count%2==1:
                break
            node = nextnode
            
        if node and even:
            node.next = even.next
        return odd.next