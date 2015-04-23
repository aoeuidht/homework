#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        if m == n:
            return m
        if m == 0:
            return 0
        mark = 1 << 31
        rst = 0
        for i in range(32):
            _m = m & mark
            _n = n & mark
            if _m == _n:
                if _m > 0:
                    rst += mark
                mark >>= 1
            else:
                break
        return rst

    def rba(self, m, n):
        r = m
        for j in range(m+1, n+1):
            r &= j
        return r

if __name__ == '__main__':
    s = Solution()
    for i in range(0, 100):
        for j in range(i+1, 99):
            #s.rangeBitwiseAnd(i, j)
            #continue
            print i, j, (s.rangeBitwiseAnd(i, j) == s.rba(i, j))
