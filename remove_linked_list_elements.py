# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prehead = ListNode(0, head)
        prev = prehead
        node = head
        while node:
            if node.val==val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return prehead.next