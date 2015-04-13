# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head:
            return head
        m1 = head
        m2 = head
        step1 = 0
        while True:
            m1 = m1.next
            m2 = m2.next
            step1 += 1
            if m2:
                m2 = m2.next
            if not m2:
                return None
            if m1 is m2:
                break
        # now count the cycle length
        step2 = 0
        while True:
            step2 += 1
            m1 = m1.next
            m2 = m2.next.next
            if m1 is m2:
                break
        c = step1 - step2
        while c > 0:
            c -= 1
            head = head.next
        while True:
            if head is m1:
                return head
            head = head.next
            m1 = m1.next
