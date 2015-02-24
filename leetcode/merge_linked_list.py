# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not (l1 and l2):
            return l1 if l1 else l2
            
        r = ListNode(0)
        h = r
        while l1 and l2:
            if (l1.val < l2.val):
                h.next = l1
                l1 = l1.next
            else:
                h.next = l2
                l2 = l2.next
            h = h.next
        if l1 or l2:
            h.next = l1 if l1 else l2
        return r.next
        
