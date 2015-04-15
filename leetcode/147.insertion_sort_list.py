#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random

from  oj_helper import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        rst = ListNode(0)
        rst.next = head
        while head:
            if head.next and (head.val <= head.next.val):
                head = head.next
            else:
                break
        if not head:
            return rst.next
        print head
        _h = head
        head = head.next
        _h.next = None

        while head:
            head_next = head.next
            prev = rst
            while (prev.next and (prev.next.val < head.val)):
                prev = prev.next
            head.next = prev.next
            prev.next = head
            head = head_next
        return rst.next

if __name__ == '__main__':
    s = Solution()
    cs = range(int(sys.argv[1]))
    random.shuffle(cs)
    head = ListNode(-1)
    oh = head
    cs = range(100)
    cs = [5] + cs
    for i in cs:
        oh.next = ListNode(i)
        oh = oh.next
    r = s.insertionSortList(head.next)
    print_list(r)
