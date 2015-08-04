#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from oj_helper import *

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        if node and node.next:
            node.val = node.next.val
            node.next = node.next.next


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
