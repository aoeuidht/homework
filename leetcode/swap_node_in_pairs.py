# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        r = ListNode(0)
        piv = r
        ctn = None
        fst, snd = None, None
        while True:
            fst = head
            snd = head.next if head else None
            if not fst:
                break
            if not snd:
                piv.next = fst
                piv = fst
                break
            else:
                ctn = snd.next
                piv.next = snd
                snd.next = fst
                piv = fst
                head = ctn
        piv.next = None
        return r.next
        
