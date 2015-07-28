#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oj_helper import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        rp, rq = self.lca_wrapper(root, p, q, [])
        lp, lq = len(rp), len(rq)
        r = None
        for i in range(min(lp, lq)):
            if rp[i] is rq[i]:
                r = rp[i]
            else:
                break
        return r

    def lca_wrapper(self, root, p, q, path):
        if not root:
            return [], []
        rstp, rstq = [], []
        if p and (root is p):
            p = None
            rstp = path + [root]

        if q and (root is q):
            q = None
            rstq = path + [root]

        if ((not p) or rstp) and ((not q) or rstq):
            return rstp, rstq

        if p or q:
            if root.left:
                _rp, _rq = self.lca_wrapper(root.left,
                                            p, q,
                                            path + [root])
                rstp = rstp if rstp else _rp
                rstq = rstq if rstq else _rq
            if ((not p) or rstp) and ((not q) or rstq):
                return rstp, rstq

            if root.right:
                _rp, _rq = self.lca_wrapper(root.right,
                                            p, q,
                                            path + [root])
                rstp = rstp if rstp else _rp
                rstq = rstq if rstq else _rq
        return rstp, rstq


if __name__ == '__main__':
    r = TreeNode(1)
    #r.left = TreeNode(2)
    r.right = TreeNode(3)

    s = Solution()
    print s.lowestCommonAncestor(r, r, r.right)
