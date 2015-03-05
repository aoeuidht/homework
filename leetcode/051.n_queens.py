#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
"""
"""
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        rst = []
        cand = range(n)
        for i in cand:
            rst = self.expand_cand(rst, cand)
        r = []
        for _r in rst:
            _t = []
            for j in _r:
                _j = ['.'] * n
                _j[j] = 'Q'
                _t.append(''.join(_j))
            r.append(_t)

        return r

    def expand_cand(self, rst, cand):
        r = []
        if not rst:
            return [[i] for i in cand]
        item_len = len(rst[0])
        for i in rst:
            for j in (set(cand) - set(i)):
                if self.chk_cand(i, j, item_len):
                    _i = i[:]
                    _i.append(j)
                    r.append(_i)
        return r

    def chk_cand(self, r_his, j, item_len):
        for i in range(item_len):
            if abs(i - item_len) == abs(r_his[i] - j):
                return False
        # check two queens
        return True

if __name__ == '__main__':
    s = Solution()
    rst = s.solveNQueens(int(sys.argv[1]))
    for r in rst:
        print '--------------------'
        for j in r:
            print j
