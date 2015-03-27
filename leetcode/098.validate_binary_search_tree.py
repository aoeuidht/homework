#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.v_wrapper(root, None, None)

    def v_wrapper(self, node, small, big):
        print node and node.val, small, big
        if not node:
            return True

        if (((small is None) or (small < node.val)) and
            ((big is None) or (node.val < big))):
            return (self.v_wrapper(node.right,
                                   node.val if (small is None) else min(node.val, small),
                                   big) and
                    self.v_wrapper(node.left,
                                   small,
                                   node.val if (big is None) else max(node.val, big)))
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    a = TreeNode(0)
    a.left = TreeNode(-1)
    print s.isValidBST(a)
