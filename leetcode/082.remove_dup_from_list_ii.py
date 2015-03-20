# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return head
            
        rtail = head
        cur = head.next
        while cur:
            if rtail.val != cur.val:
                rtail = rtail.next
                rtail.val = cur.val
            cur = cur.next
        rtail.next = None
        return head
        
