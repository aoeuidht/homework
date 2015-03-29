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
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        return self.b_wrapper(preorder, 0, inorder, 0, len(preorder))

    def b_wrapper(self, preorder, pl, inorder, il, l):
        if l < 1:
            return None
        elif l == 1:
            return TreeNode(preorder[pl])
        root = TreeNode(preorder[pl])

        # find the idx
        idx = inorder.index(root.val)
        left_len = idx - il
        root.left = self.b_wrapper(preorder, pl+1, inorder, il, left_len)
        root.right = self.b_wrapper(preorder, pl+left_len+1, inorder, idx+1, l-left_len-1)
        return root


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
    sys.setrecursionlimit(15)
    s = Solution()
    print_bst(s.buildTree([1, 2, 3], [3, 2, 1]))
    print_bst(s.buildTree([1, ], [3, ]))
    print_bst(s.buildTree([20, 3, 9, 15, 7], [9, 3, 15, 20, 7]))
