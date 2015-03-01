#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        al = len(A)
        if al < 3:
            return 0
        lmax = [0] * al
        rmax = [0] * al
        for i in range(1, al-1):
            lmax[i] = max(A[i-1], lmax[i-1])
            rmax[al-i-1] = max(A[al-i], rmax[al-i])
        rst = 0
        for i in range(1, al-1):
            diff = min(lmax[i], rmax[i]) - A[i]
            rst += (diff if diff > 0 else 0)
        return rst
if __name__ == '__main__':
    s = Solution()
    print s.trap(map(int, sys.argv[1].split(',')) if sys.argv[1] else [])
