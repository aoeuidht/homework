#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        al = len(A)
        if al == 0:
            return 0
        elif al == 1:
            return A[0]
        rst = A[0]
        cur = rst
        for _i in range(1, al):
            i = A[_i]
            if cur >= 0:
                cur += i
                if cur < 0:
                    cur = 0
                if cur > rst:
                    rst = cur
                    continue

            # cur < 0
            else:
                if i >= 0:
                    cur = i
                else:
                    cur = max(cur, i)
                if cur > rst:
                    rst = cur
        return rst

if __name__ == '__main__':
    s = Solution()
    print s.maxSubArray(map(int, sys.argv[1].split(',')))
