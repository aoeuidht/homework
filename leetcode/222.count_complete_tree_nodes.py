#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from oj_helper import *

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        # calc the height
        tree_height = 0
        h = root
        while h:
            tree_height += 1
            h = h.left

        if tree_height <= 1:
            return tree_height
        return self.count_note_with_height(root, tree_height) + (2 ** (tree_height - 1)) - 1

    def count_note_with_height(self, root, tree_height):
        if tree_height == 1:
            return 1
        # check the right son of the left tree
        left_height = 1
        h = root.left
        while h:
            left_height += 1
            h = h.right

        left_count = 0
        h = root.left
        # on the left
        if left_height == tree_height:
            left_count = 2 ** (tree_height - 2)
            h = root.right
        return left_count + (self.count_note_with_height(h, tree_height -1)
                             if h else 0)

if __name__ == '__main__':
    s = Solution()
    h = TreeNode(1)
    print s.countNodes(h)
    h.left = TreeNode(2)
    print s.countNodes(h)
    h.right = TreeNode(2)
    print s.countNodes(h)

    h.left.left = TreeNode(2)
    print s.countNodes(h)
    h.left.right = TreeNode(2)
    print s.countNodes(h)

    h.right.left = TreeNode(2)
    print s.countNodes(h)
    h.right.right = TreeNode(2)
    print s.countNodes(h)
