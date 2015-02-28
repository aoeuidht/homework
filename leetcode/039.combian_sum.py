#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        r = self.c_wrapper(candidates, 0, len(candidates) -1, target, [])
        if r and (not (type(r[0]) is list)):
            return [r]
        return r

    def c_wrapper(self, cands, lo, hi, target, prev_rst=None):
        if target == 0:
            return prev_rst
        elif target < 0:
            return []

        if lo > hi:
            return []
        cand = cands[lo]
        if cand > target:
            return []
        elif cand == target:
            return prev_rst + [cand]
        _r = []
        for i in range(1, (target / cand) + 1):
            __r = self.c_wrapper(cands, lo+1, hi, target-cand*i, prev_rst + [cand] * i)
            if __r:
                if type(__r[0]) is list:
                    _r += __r
                else:
                    _r.append(__r)
        __r = self.c_wrapper(cands, lo+1, hi, target, prev_rst)
        if __r:
            if type(__r[0]) is list:
                _r += __r
            else:
                _r.append(__r)
        return _r

if __name__ == '__main__':
    s = Solution()
    print s.combinationSum(map(int, sys.argv[1].split(',')),
                           int(sys.argv[2]))
