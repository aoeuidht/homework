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
    def buildTree(self, inorder, postorder):
        if not postorder:
            return None
        return self.b_wrapper(inorder, 0, postorder, 0, len(inorder))

    def b_wrapper(self, inorder, il, postorder, pl, l):
        if l < 1:
            return None
        elif l == 1:
            return TreeNode(postorder[pl])
        root = TreeNode(postorder[pl+l-1])

        # find the idx
        idx = inorder.index(root.val)
        left_len = idx - il
        root.left = self.b_wrapper(inorder,
                                   il,
                                   postorder,
                                   pl,
                                   left_len)
        root.right = self.b_wrapper(inorder,
                                    idx+1,
                                    postorder,
                                    pl+left_len,
                                    l-left_len-1)
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
    s = Solution()
    print_bst(s.buildTree([3, 15, 7, 20, 8, 9],
                          [3, 7, 15, 8, 9, 20]))
