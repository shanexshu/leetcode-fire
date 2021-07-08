class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = ListNode(5)
        dummypointer = dummy
        l1pointer = l1
        l2pointer = l2

        # l1 = [1,2,3]
        # l2 = [3,3,4]
        # dummypointer -> 1 ->2->3

        if l1pointer == None and l2pointer == None: return None
        while (l1pointer and l2pointer):
            if (l1pointer.val <= l2pointer.val): #
                dummypointer.next = l1pointer
                l1pointer = l1pointer.next
            else:
                dummypointer.next = l2pointer
                l2pointer = l2pointer.next
            dummypointer = dummypointer.next

        if(l2pointer):
            dummypointer.next = l2pointer
        if(l1pointer): #l2pointer is null
            dummypointer.next = l1pointer
        return dummy.next