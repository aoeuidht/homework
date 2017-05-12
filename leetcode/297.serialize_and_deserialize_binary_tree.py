#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from oj_helper import *


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        cands = [root]
        node_list = []
        while cands:
            node = cands.pop(0)
            node_list.append(node.val if node else '')
            if node:
                cands.append(node.left)
                cands.append(node.right)
        return ','.join(map(str, node_list))

    def de_token(self, rst):
        """

        Arguments:
        - `self`:
        - `rst`:
        """
        for item in rst.split(','):
            yield item

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        tokens = self.de_token(data)
        root = TreeNode(tokens.next())
        nq = [root]

        while nq:
            node = nq.pop(0)
            try:
                l = tokens.next()
                r = tokens.next()
                if l:
                    node.left = TreeNode(l)
                    nq.append(node.left)
                if r:
                    node.right = TreeNode(r)
                    nq.append(node.right)
            except:
                break
        return root


if __name__ == '__main__':
    r = TreeNode(0)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    r.right.left = TreeNode(4)
    r.right.right = TreeNode(5)

    c = Codec()
    print_bst(r)
    r = TreeNode(0)
    s = c.serialize(r)
    print s
    root = c.deserialize(s)
    print_bst(root)

    print(c.deserialize(''))
