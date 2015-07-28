#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oj_helper import *

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not (head and head.next):
            return True

        _slow, _fast = head, head.next

        while True:
            if _fast and _fast.next and _fast.next.next:
                _fast = _fast.next.next
                _slow = _slow.next
                continue

            # if _fast is not the end, break on next step
            if _fast.next:
                _slow = _slow.next
            break

        # revert the tailing half
        piv = _slow
        _slow = _slow.next
        piv.next = None
        piv = None
        while _slow:
            o = _slow
            _slow = _slow.next
            o.next = piv
            piv = o

        while piv:
            if piv.val == head.val:
                piv = piv.next
                head = head.next
                continue
            return False
        return True


if __name__ == '__main__':

    s = Solution()
    head = ListNode(-1)
    piv = head
    for i in range(20):
        head = ListNode(-1)
        piv = head
        for j in range(i):
            o = ListNode(j)
            piv.next = o
            piv = o

        print '------------', i, '------------'
        print s.isPalindrome(head)
