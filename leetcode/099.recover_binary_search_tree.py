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
    # @return nothing, modify the binary tree in-place instead.
    def recoverTree(self, root):
        rst = [None, None, None]
        self.t_wrapper((root, None, None), rst)
        rst[1][0].val, rst[2][0].val = rst[2][0].val, rst[1][0].val
        return root

    # info is a (node, parent, position) tuple
    # rst is [prev, r0, r1]
    def t_wrapper(self, info, rst):
        node, parent, position = info
        if not node:
            return
        if node.left:
            self.t_wrapper((node.left, node, 0), rst)
        if rst[0] == None:
            rst[0] = info
        elif rst[0][0].val > node.val:
            if rst[1] == None:
                rst[1] = rst[0]
            rst[2] = info
        rst[0] = info
        if node.right:
            self.t_wrapper((node.right, node, 1), rst)

def print_bst(root, prefix=' '):
    print prefix, root.val
    if root.right:
        if root.left:
            rprefix = prefix + ' | '
        else:
            rprefix = prefix + '   '
        print rprefix[:-1], '\\'
        print_bst(root.right, rprefix)
    elif root.left:
        print prefix, '|'
    if root.left:
        print_bst(root.left, prefix=prefix)


if __name__ == '__main__':
    s = Solution()
    a = TreeNode(5)
    a.right = TreeNode(8)
    a.left = TreeNode(3)
    a.left.left = TreeNode(2)
    a.left.right = TreeNode(7)
    a.right.left = TreeNode(4)
    a.right.right = TreeNode(9)
    a = TreeNode(5)
    a.right = TreeNode(3)
    a.left = TreeNode(6)
    r = s.recoverTree(a)
    print_bst(r)
