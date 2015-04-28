#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        _head = ListNode(0)
        _head.next = head
        h = _head
        while h:
            if not h.next:
                break
            if h.next.val == val:
                h.next = h.next.next
            else:
                h = h.next
        return _head.next

if __name__ == '__main__':
    s = Solution()
