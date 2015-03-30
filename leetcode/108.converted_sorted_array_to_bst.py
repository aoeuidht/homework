#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from oj_helper import *

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return None
        return self.s_wrapper(num, 0, len(num)-1)

    def s_wrapper(self, num, lo, hi):
        if lo > hi:
            return None
        elif lo == hi:
            return TreeNode(num[lo])

        idx = lo + self.get_root_idx(hi-lo+1, 1)
        root = TreeNode(num[idx])
        root.left = self.s_wrapper(num, lo, idx-1)
        root.right = self.s_wrapper(num, idx+1, hi)
        return root

    def get_root_idx(self, n, batch):
        idx = 0
        batch = 2
        hb = batch / 2
        no = n
        n -= 1
        while n > 0:
            if n > hb:
                idx += hb
            else:
                idx += n
            n -= batch
            hb = batch
            batch *= 2
        return idx

if __name__  == '__main__':
    sys.setrecursionlimit(15)
    s = Solution()
    print_bst(s.sortedArrayToBST(range(int(sys.argv[1]))))
