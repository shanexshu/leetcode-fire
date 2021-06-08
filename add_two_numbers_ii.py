# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def reverseLL(head):
            prev = None
            while head:
                nextnode = head.next
                head.next = prev
                prev = head
                head = nextnode
            return prev
        
        def addLL(head1, head2):
            node1, node2 = head1, head2
            ans = ListNode(-1)
            node = ans
            carry = 0
            while node1 and node2:
                val = node1.val + node2.val + carry
                carry = --(val>=10)
                val %= 10
                node.next = ListNode(val)
                node = node.next
                node1, node2 = node1.next, node2.next
            if node1:
                node.next = addLL(ListNode(carry), node1)
            elif node2:
                node.next = addLL(ListNode(carry), node2)
            else:
                if carry:
                    node.next = ListNode(carry)
            return ans.next
        
        revl1, revl2 = reverseLL(l1), reverseLL(l2)
        
        
        
        return reverseLL(addLL(revl1, revl2))