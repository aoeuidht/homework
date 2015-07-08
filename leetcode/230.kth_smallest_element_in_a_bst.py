#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from oj_helper import *

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        _, rst = self.k_wrapper(root, k)
        return rst

    # return a tuple, (the-number-of-nodes, the-result-if-got)
    # remember k start at 1 here
    def k_wrapper(self, root, k):
        if not root:
            return (0, None)

        cntl, rst = self.k_wrapper(root.left, k)
        if not (rst is None):
            return k, rst
        # just ok?
        if cntl == (k - 1):
            return k, root.val
        cntr, rst = self.k_wrapper(root.right, k - 1 - cntl)
        if not (rst is None):
            return k, rst
        return 1 + cntl + cntr, None

if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    s = Solution()
    print_bst(root)
    print s.kthSmallest(root, 1)
    print s.kthSmallest(root, 2)
    print s.kthSmallest(root, 3)
    print s.kthSmallest(root, 4)
    print s.kthSmallest(root, 5)
    print s.kthSmallest(root, 6)
    print s.kthSmallest(root, 7)
