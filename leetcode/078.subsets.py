#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    def __init__(self):
        self.rst = []
        self.sl = 0

    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        if not S:
            return []
        S.sort()
        self.sl = len(S)
        cand = []
        self.sub_wrapper(S, cand, 0)
        def lst_comp(l1, l2):
            ll1 = len(l1)
            ll2 = len(l2)
            if ll1 != ll2:
                return ll1 - ll2
            return 1 if l1 > l2 else -1
        return sorted(self.rst, cmp=lst_comp)

    def sub_wrapper(self, S, cand, l, dup_chon=False):
        n = S[l]
        dup = False
        if (l > 0) and (S[l-1] == n):
            dup = True

        if l == (self.sl -1):
            self.rst.append(sorted(cand))
            if not (dup and (not dup_chon)):
                cand.append(n)
                self.rst.append(sorted(cand))
                cand.pop()
            return

        self.sub_wrapper(S, cand, l+1, False)
        if not (dup and (not dup_chon)):
            cand.append(n)
            self.sub_wrapper(S, cand, l+1, True)
            cand.pop()

if __name__ == '__main__':
    s = Solution()
    r = s.subsets(map(int, sys.argv[1:]))
    print r
