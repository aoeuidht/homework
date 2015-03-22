# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if not head:
            return head
            
        lh, bh = ListNode(0), ListNode(0)
        lt = lh
        bt = bh
        
        while head:
            if head.val < x:
                lt.next = head
                lt = lt.next
            else:
                bt.next = head
                bt = bt.next
            head = head.next
        bt.next = None
        lt.next = bh.next
        return lh.next
        
