#!/usr/bin/env python

import sys

from oj_helper import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        # step 1. count the list number
        oh = head
        list_cnt = 0
        while oh:
            list_cnt += 1
            oh = oh.next
        if list_cnt < 3:
            return
        # step 2. keep the 1st half
        # skip the first half
        cnt = 0
        mid = (list_cnt + 1) / 2
        oh = head
        _p, piv = None, oh
        while cnt < mid:
            cnt += 1
            _p, piv = piv, piv.next
        _p.next = None

        tmp = piv.next
        piv.next = None
        while tmp:
            tmp_next = tmp.next
            tmp.next = piv
            piv = tmp
            tmp = tmp_next
        print_list(oh)
        print_list(piv)
        # step 4. rebuild the list
        tmp = head
        c, n = piv, head.next
        while True:
            if not c:
                tmp.next = n
                break
            if not n:
                tmp.next = c
                break
            tmp.next = c
            tmp = tmp.next
            c, n = n, c.next
        print_list(head)
if __name__ == '__main__':
    head = ListNode(0)
    oh = head
    for i in range(1, int(sys.argv[1])):
        oh.next = ListNode(i)
        oh = oh.next

    s =Solution()
    r = s.reorderList(head)
