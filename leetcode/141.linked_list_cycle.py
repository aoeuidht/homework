# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False
        m1 = head
        m2 = head
        while True:
            m1 = m1.next
            m2 = m2.next
            if m2:
                m2 = m2.next
            if not m2:
                return False
            if m1 == m2:
                return True
