#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    def __init__(self):
        self.sl = 0
        self.S = None

    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        if not S:
            return []
        S.sort()
        self.S = S
        self.sl = len(S)

        return self.s_wrapper(1, [[]], False) + self.s_wrapper(1, [[S[0]]], True)

    def s_wrapper(self, idx, rst, use_value):
        if idx == self.sl:
            return rst

        dup = (self.S[idx] == self.S[idx-1])
        _rst = [i + [self.S[idx]] for i in rst]
        rr = self.s_wrapper(idx+1, _rst, True)
        if (not dup) or (not use_value):
            rl = self.s_wrapper(idx+1, rst, False)
            return rl + rr
        else:
            return rr

if __name__ == '__main__':
    s = Solution()
    print s.subsetsWithDup(map(int,
                               sys.argv[1].split(',')))
