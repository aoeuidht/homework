# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        m, n = n, m
        if m <= n:
            return head
            
        p = ListNode(0)
        p.next = head
        it = p  # the initinal tail
        rh = None # the reverse head
        rt = None # the reverse tail

        i = 1
        while head:
            tmp = head
            head = head.next
            if i == n-1:
                it = tmp
            elif i == n:
                rh = tmp
                rt = tmp
            elif i > n:
                tmp.next = rh
                rh = tmp
                if i == m:
                    break
            i += 1
        rt.next = head
        it.next = rh
        return p.next
                
        
