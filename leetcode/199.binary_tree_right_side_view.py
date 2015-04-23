#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from oj_helper import *

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        rst = []
        rc = 0
        self.t_travel(root, 1, rst)
        return rst

    def t_travel(self, root, h, rst):
        if not root:
            return
        l = len(rst)
        if h > l:
            rst.append(root.val)
        self.t_travel(root.right, h+1, rst)
        self.t_travel(root.left, h+1, rst)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(3)
    #root.right.right = TreeNode(4)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(7)
    print s.rightSideView(root)
