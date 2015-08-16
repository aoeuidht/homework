#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oj_helper import *

class Solution:
    def __init__(self):
        """

        Arguments:
        - `self`:
        """
        self.rst = []

    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        self.btp_wrapper(root, [])
        return self.rst

    def btp_wrapper(self, node, prefix):
        if not node:
            return
        prefix.append(node.val)
        if node.left or node.right:
            if node.left:
                self.btp_wrapper(node.left, prefix)
            if node.right:
                self.btp_wrapper(node.right, prefix)
        else:
            self.rst.append('->'.join(map(str, prefix)))
        prefix.pop()

if __name__ == '__main__':
    s = Solution()

    h = TreeNode(1)
    h.left = TreeNode(2)
    h.right = TreeNode(3)
    h.left.right = TreeNode(5)

    print s.binaryTreePaths(h)
