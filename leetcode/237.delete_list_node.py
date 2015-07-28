#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from oj_helper import *

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        # len is 0 or 1
        if (not node) or (not node.next):
            return

        f, piv = node, node.next

        while piv.next:
            f, piv = f.next, piv.next

        f.val = piv.val
        f.next = None


if __name__ == '__main__':
    h = ListNode(-10)
    p = h
    for i in range(int(sys.argv[1])):
        p.next = ListNode(i)
        p = p.next

    s = Solution()
    print '---------------'
    print_list(h)
    s.deleteNode(h)
    print_list(h)
