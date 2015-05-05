# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        rh = ListNode(0)
        head_next = head
        while head_next:
            hc = head_next
            head_next = head_next.next
            
            hc.next = rh.next
            rh.next = hc
        return rh.next
        
