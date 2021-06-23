# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # save the head of the original
        sent = ListNode()
        sent.next = head
        
        # traverse to left position
        i = 1
        prev = None
        while head and i<left:
            prev = head
            head = head.next
            i += 1
        
        # i = left
        # reverse up to right position
        p = None
        rhead = head
        while head and i<=right:
            nextnode = head.next
            head.next = p
            p = head
            head = nextnode
            i += 1
            
        # head now at next of right position
        if head:
            rhead.next = head
        
        if prev:
            prev.next = p
        else:
            sent.next = p
        
        return sent.next
            
        # 1->    2->3->4->5
        #  5<-2<-3<-4<-1
        
        # 3->5
        # 3