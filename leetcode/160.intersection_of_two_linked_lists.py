# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        oa, ac = headA, 0
        ob, bc = headB, 0
        am, bm = None, None
        while oa:
            ac += 1
            am = oa
            oa = oa.next
        while ob:
            bc += 1
            bm = ob
            ob = ob.next
        if not (am is bm):
            return None

        oa, ob = headA, headB
        if ac > bc:
            for i in range(ac-bc):
                oa = oa.next
        else:
            for i in range(bc-ac):
                ob = ob.next
        while True:
            if oa is ob:
                return oa
            oa = oa.next
            ob = ob.next
