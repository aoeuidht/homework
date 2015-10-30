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
        rst = [str(root.val)]
        for r in self.s_wrapper(root):
            rst.append('null' if (r is None) else str(r))
        return ','.join(rst)

    def s_wrapper(self, root):
        if not root:
            return
        l, r = root.left, root.right
        yield l.val if l else None
        yield r.val if r else None
        for y in self.s_wrapper(l):
            yield y
        for y in self.s_wrapper(r):
            yield y

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nvs = data.split(',')
        if not nvs:
            return None
        nq = [TreeNode(nvs[0])]

        piv = 0
        vl = len(nvs)

        # 0: skip, 1: left, 2 right
        pos = 0
        for v in nvs:
            if pos == 0:
                pos = 1
                continue
            # left
            if v == 'null':
                tn = None
            else:
                tn = TreeNode(int(v))
            if pos == 1:
                nq[piv].left = tn
                pos = 2
            else:
                nq[piv].right = tn
                piv += 1
                pos = 1

            if tn:
                nq.append(tn)
        return nq[0]

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
    root = c.deserialize(s)
    print_bst(root)

    print_bst(c.deserialize(''))
