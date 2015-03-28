#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if id(p) == id(q):
            return True
        if (not p) or (not q):
            return False
        return ((p.val == q.val) and
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
        return False

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
    r = s.generateTrees(int(sys.argv[1]))
    for _r in r:
        print_bst(_r)
        print '-' * 30

    for i in range(20):
        print i, len(s.generateTrees(i))
