#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        rst = tail = None
        g = 0
        while l1 or l2:
            r = g
            n1, n2 = None, None
            b1, b2 = True, True
            if l1:
                r += l1.val
                n1 = l1.next
                b1 = False
            if l2:
                r += l2.val
                n2 = l2.next
                b2 = False
            g = r / 10
            r %= 10

            _n = ListNode(r)
            if not rst:
                rst = _n
                tail = _n
            else:
                tail.next = _n
                tail = _n
            l1, l2 = n1, n2
            if g:
                continue
            if b1:
                tail.next = l2
                break
            if b2:
                tail.next = l1
                break
        if g:
            _n = ListNode(g)
            tail.next = _n
        return rst
