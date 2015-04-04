#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oj_helper import *

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        sum, _ = self.s_wrapper(root)
        if root and (root.val > sum):
            return root.val
        return sum

    def s_wrapper(self, root):
        if not root:
            return 0, 0
        sum_l, single_l = self.s_wrapper(root.left)
        sum_r, single_r = self.s_wrapper(root.right)

        single = root.val
        _sum = root.val
        if root.left and root.right:
            single = max(single_l, single_r, 0) + root.val
            _sum = max(sum_l, sum_r,
                       single_l+single_r+root.val,
                       single_r + root.val,
                       single_l + root.val)
        elif root.left:
            single = max(root.val, root.val + single_l)
            _sum = max(sum_l, single_l+root.val, root.val)
        elif root.right:
            single = max(root.val, root.val + single_r)
            _sum = max(sum_r, single_r+root.val, root.val)
        return _sum, single

if __name__ == '__main__':
    s = Solution()
    a = TreeNode(1)
    a.left = TreeNode(-2)
    a.right = TreeNode(3)
    print s.maxPathSum(a)
