#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '%d -> ' % self.val

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if k < 1:
            return head
        n_tail = head
        o_tail = None
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            if cnt == k+1:
                o_tail = cur
            elif cnt > k:
                o_tail = o_tail.next
                n_tail = n_tail.next
            cur = cur.next
        if cnt < 2:
            return head
        if not o_tail:
            return self.rotateRight(head, k % cnt)
        n_head = n_tail.next
        n_tail.next = None
        o_tail.next = head
        return n_head

if __name__ == '__main__':
    s = Solution()
    h = ListNode(0)
    cur = h
    for i in range(1, int(sys.argv[1])+1):
        n = ListNode(i)
        cur.next = n
        cur = n
    r = s.rotateRight(h, int(sys.argv[2]))
    while r:
        print r
        r = r.next
