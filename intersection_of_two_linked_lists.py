# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA = headA
        nodeB = headB
        scans = 0
        while nodeA!=nodeB:
            if scans>1: return None
            if nodeA:
                nodeA = nodeA.next
            if not nodeA: 
                nodeA = headB
                scans += 1
            if nodeB:
                nodeB = nodeB.next
            if not nodeB: 
                nodeB = headA
        
        return nodeA