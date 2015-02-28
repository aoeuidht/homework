#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        r = self.c_wrapper(candidates, 0, len(candidates) -1, target, [])
        rst = []
        rd = set()
        for _r in r:
            _r.sort()
            k = '-'.join(map(str, _r))
            if k not in rd:
                rd.add(k)
                rst.append(_r)
        return rst

    def c_wrapper(self, cands, lo, hi, target, prev_rst, rd=set()):
        if target == 0:
            return prev_rst

        if lo > hi:
            return []
        _r = []
        cand = cands[lo]
        if cand > target:
            return []
        elif cand == target:
            return [prev_rst + [cand]]

        __r = self.c_wrapper(cands, lo+1, hi, target, prev_rst)
        if __r:
            if type(__r[0]) is list:
                _r += __r
            else:
                _r.append(__r)
        __r = self.c_wrapper(cands, lo+1, hi, target-cand, prev_rst + [cand])
        if __r:
            if type(__r[0]) is list:
                _r += __r
            else:
                _r.append(__r)
        return _r
if __name__ == '__main__':
    s = Solution()
    print s.combinationSum2(map(int, sys.argv[1].split(',')),
                           int(sys.argv[2]))
