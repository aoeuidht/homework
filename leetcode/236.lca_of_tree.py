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
        rp, rq = self.lca_wrapper(root, p, q)
        print rp, rq
        print_bst(rp)
        return rp

    def lca_wrapper(self, root, p, q):
        if not root:
            return None, None

        rp, rq = None, None
        if root is p:
            p = None
            rp = root

        if root is q:
            q = None
            rq = root

        # if we still have to look further
        if (p and (not rp))  or (q and (not rq)):
            # left
            if root.left:
                _rp, _rq = self.lca_wrapper(root.left,
                                            p, q)
                if p:
                    p = None if _rp else p
                    rp = _rp
                if q:
                    q = None if _rq else q
                    rq = _rq

        if (p and (not rp))  or (q and (not rq)):
            # right
            if root.right:
                _rp, _rq = self.lca_wrapper(root.right,
                                            p, q)
                rp = _rp if p else rp
                rq = _rq if q else rq
        if rp and rq and (not (rp is rq)):
            return root, root
        return rp, rq

if __name__ == '__main__':
    r = TreeNode(1)
    r.left = TreeNode(2)
    #r.right = TreeNode(3)

    s = Solution()
    print s.lowestCommonAncestor(r, r.left, r)
