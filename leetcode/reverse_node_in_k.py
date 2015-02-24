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

    def __str__(self):
        return '(%d, %s None)' % (self.val, ('not' if self.next else ''))

    def __repr__(self):
        return '(%d, %s None)' % (self.val, ('not' if self.next else ''))

    def pnt(self):
        r = self
        while r:
            print r, r.val
            r = r.next
        print '----- done ----'

class Solution:
    def reverseKGroup(self, head, k):
        if (not head) or (k == 1):
            return head
        buf = [None] * k
        i = 0
        r = ListNode(0)
        piv = r
        while head:
            buf[i] = head
            head = head.next
            i += 1
            if i == k:
                i = 0
                # reverse all keys
                buf[0].next = None
                for j in range(1, k):
                    buf[j].next = buf[j-1]
                piv.next = buf[k-1]
                piv = buf[0]
                buf = [None] * k
        piv.next = buf[0]
        return r.next

if __name__ == '__main__':
    s = Solution()
    vs = sys.argv[1].split(',')
    j = None
    t = j
    for i in vs:
        if not j:
            j = ListNode(int(i))
            t = j
        else:
            t.next = ListNode(int(i))
            t = t.next
    j.pnt()
    #print 'the ps are:', ps
    r = s.reverseKGroup(j, int(sys.argv[2]))
    if r:
        r.pnt()
