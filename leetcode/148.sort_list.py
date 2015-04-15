#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random

from  oj_helper import *
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        r, _ = self.s_wrapper(head)
        return r

    def s_wrapper(self, head):
        if not head:
            return None, None
        lhead, shead = ListNode(0), ListNode(0)
        ltail, stail = None, None
        ehead, etail = ListNode(0), None
        lc, sc = 0, 0
        #shead.next = head
        piv = head.val

        ehead.next = head
        etail = head

        oh = head
        head = head.next
        oh.next = None

        while head:
            tmp = head.next
            # we use bigger here to make sure that
            # small list will not be blank
            if head.val > piv:
                head.next = lhead.next
                lhead.next = head
                ltail = ltail if ltail else head
                lc += 1
            elif head.val < piv:
                head.next = shead.next
                shead.next = head
                sc += 1
                stail = stail if stail else head
            else:
                head.next = ehead.next
                ehead.next = head
            head = tmp
        #print_list(shead.next)
        #print_list(lhead.next)
        # sort the small ones
        batch = 100
        if sc > batch:
            _shead, stail = self.s_wrapper(shead.next)

        elif sc > 1:
            _shead, stail = self.insertionSortList(shead.next)
        else:
            _shead = shead.next
        shead.next = _shead

        # sort the big ones
        if lc > batch:
            _lhead, ltail = self.s_wrapper(lhead.next)
        elif lc > 1:
            _lhead, ltail = self.insertionSortList(lhead.next)
        else:
            _lhead = lhead.next
        lhead.next = _lhead
        # join small and equal
        if shead.next:
            stail.next = ehead.next
        else:
            shead.next = ehead.next
        stail = etail


        if lhead.next:
            stail.next = lhead.next
        else:
            ltail = stail
        return shead.next, ltail

    def insertionSortList(self, head):
        rst = ListNode(0)
        tail = None
        while head:
            head_next = head.next
            prev = rst
            while (prev.next and (prev.next.val < head.val)):
                prev = prev.next
            head.next = prev.next
            prev.next = head
            if not head.next:
                tail = head
            head = head_next
        tail.next = None
        return rst.next, tail

if __name__ == '__main__':
    sys.setrecursionlimit(1250)
    s = Solution()
    piv = ListNode(0)
    """
    oh = piv
    cs = range(1000)
    random.shuffle(cs)
    cs = [3, 2, 1]
    for i in cs:
        oh.next = ListNode(i)
        oh = oh.next
    h = s.sortList(piv.next)
    print_list(h)
    """
    head = piv
    with open('148.cases.txt') as f:
        f.readline()
        cand = map(int, f.readline().split(','))
        for c in cand:
            head.next = ListNode(c)
            head = head.next
        r = s.sortList(piv.next)
        print_list(r)
