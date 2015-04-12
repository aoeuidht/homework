#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(root):
    rst = []
    while root:
        rst.append(root.val)
        root = root.next
    print ' --> '.join(map(str, rst))
