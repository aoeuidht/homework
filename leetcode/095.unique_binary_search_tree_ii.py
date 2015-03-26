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
    def __init__(self):
        self.c = {}

    # @return a list of tree node
    def generateTrees(self, n):
        return self.g_wrapper(1, n)

    def g_wrapper(self, lo, hi):
        rst = []
        k = '%d-%d' % (lo, hi)
        if self.c.has_key(k):
            return self.c[k]

        if lo > hi:
            return [None]
        elif lo == hi:
            rst = [TreeNode(lo)]
            self.c[k] = rst
            return rst
        elif lo + 1 == hi:
            h = TreeNode(lo)
            h.right = TreeNode(hi)
            rst.append(h)
            h = TreeNode(hi)
            h.left = TreeNode(lo)
            rst.append(h)
            self.c[k] = rst
            return rst

        for i in range(lo, hi+1):
            _l = self.g_wrapper(lo, i-1)
            _r = self.g_wrapper(i+1, hi)
            for __l in _l:
                for __r in _r:
                    h = TreeNode(i)
                    h.left = __l
                    h.right = __r
                    rst.append(h)
        self.c[k] = rst
        return rst




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
