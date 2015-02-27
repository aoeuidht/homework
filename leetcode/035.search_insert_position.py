#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        return self.i_wrapper(A, 0, len(A)-1, target)

    def i_wrapper(self, A, lo, hi, target):
        if (hi - lo) < 5:
            for i in range(lo, hi+1):
                if A[i] >= target:
                    return i
            return hi+1
        mid_idx = (lo + hi) / 2
        mid_val = A[mid_idx]
        if mid_val == target:
            return mid_idx
        elif mid_val > target:
            return self.i_wrapper(A, lo, mid_idx-1, target)
        return self.i_wrapper(A, mid_idx+1, hi, target)

if __name__ == '__main__':
    s = Solution()
    print s.searchInsert(map(int, sys.argv[1].split(',')), int(sys.argv[2]))
