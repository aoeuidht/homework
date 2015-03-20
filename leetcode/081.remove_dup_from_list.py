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
        rst = ListNode(0)
        rst.next = head
        rtail = rst
        pv = head.val
        
        cur = head.next
        a = True
        while cur:
            cv = cur.val
            if (cv != pv):
                if a:
                    rtail = rtail.next
                    rtail.val = pv
                a = True
            else:
                a = False
            pv = cv    
            cur = cur.next
        if a:
            rtail = rtail.next
            rtail.val = pv
        rtail.next = None
        return rst.next
        
