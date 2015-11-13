#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from oj_helper import print_list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nl = len(nums)

        # add last one
        piv_node = ListNode(0)
        piv_node.next = ListNode([nums[-1], 0])

        max_val, min_val = nums[-1], nums[-1]

        for idx in range(nl-2, -1, -1):
            val = nums[idx]
            h = piv_node.next
            rst = 0
            if val >= max_val:
                max_val, rst = val, 0
            elif val <= min_val:
                min_val = val
                rst = h.val[1] + (0 if (val == h.val[0]) else 1)
            else:
                while h:
                    if val > h.val[0]:
                        h = h.next
                        continue
                    if val == h.val[0]:
                        rst = h.val[1]
                    elif val < h.val[0]:
                        rst = h.val[1]+1
                    break
            # insert to the linked list
            n = ListNode([val, rst])
            h = piv_node
            while h:
                if not h.next:
                    h.next = n
                    break
                if h.next.val[1] > n.val[1]:
                    h = h.next
                    continue
                # insert now
                n.next, h.next = h.next, n
                break
            #print_list(piv_node.next)
        return piv_node.next.val[1] + 1

if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
    print s.lengthOfLIS(range(-1, -2501, -1))
    print s.lengthOfLIS(range(0, 2501))
