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
    def rebuild_lists(self, a, lo, hi):
        if not a[lo]:
            return lo+1, hi
        if lo >= hi:
            return lo, hi
        # use insertion sort here
        for i in range(lo+1, hi+1):
            cr = self.cmp_node(a[lo+i-1], a[lo+i])
            if cr > 0:
                a[lo+i-1], a[lo+i] = a[lo+i], a[lo+i-1]
            else:
                break
        return lo, hi

    def cmp_node(self, n1, n2):
        if not n1:
            return -1 if n2 else 0
        return (n1.val - n2.val) if n2 else 1

    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        nl = len(lists)
        if nl == 0:
            return None
        elif nl == 1:
            return lists[0]
        rst = ListNode(0)
        head = rst
        lists = sorted(lists, cmp=self.cmp_node)
        l, r = 0, nl-1
        while l <= r:
            while not lists[l]:
                l, r = self.rebuild_lists(lists, l, r)
                if l > r:
                    break
                continue
            if l > r:
                break
            elif l == r:
                head.next = lists[l]
                break
            head.next = lists[l]
            head = head.next
            if head:
                lists[l] = head.next
            l, r = self.rebuild_lists(lists, l, r)

        return rst.next

if __name__ == '__main__':
    s = Solution()
    ps = []
    vs = sys.argv[1][1:-1].split('},{')
    for v in vs:
        j = None
        t = j
        if v:
            for i in v.split(','):
                if not j:
                    j = ListNode(int(i))
                    t = j
                else:
                    t.next = ListNode(int(i))
                    t = t.next
        ps.append(j)
    #print 'the ps are:', ps
    r = s.mergeKLists(ps)
    """
    if r:
        r.pnt()"""
