#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # [lo, hi) are reachable
        lo, hi = 0, 1
        al = len(A)
        if al < 2:
            return True
        while True:
            _h = hi
            for i in range(lo, hi):
                _h = (A[i]+i+1) if (A[i]+i+1) > _h else _h
            if _h >= al:
                return True
            if _h <= hi:
                return False
            lo, hi = hi, _h
            print lo, hi
        return False

if __name__ == '__main__':
    s = Solution()
    print s.canJump(map(int, sys.argv[1].split(',')))
