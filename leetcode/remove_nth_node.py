# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        lst = [head] * n
        piv = 0
        parent = head
        _h = head
        while _h:
            parent = lst[piv]
            lst[piv] = _h
            piv += 1
            piv %= n
            _h = _h.next
        # now the piv is the one to remove
        if lst[piv] == head:
            return head.next
        parent.next = lst[piv].next
        return head
