#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def jump(self, A):
        al = len(A)
        if al < 2:
            return 0
        lo, hi = 0, 1
        for i in range(1, al):
            lo, hi = hi, max([x+y for x, y in zip(range(lo, hi), A[lo:hi])]) + 1
            if hi >= al:
                return i


if __name__ == '__main__':
    s = Solution()
    print s.jump(map(int, sys.argv[1].split(',')))
