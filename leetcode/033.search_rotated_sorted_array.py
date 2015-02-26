#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        return self.s_wrapper(A, 0, len(A)-1, target)

    def s_wrapper(self, A, lo, hi, target):
        if (hi - lo) < 100:
            for i in range(lo, hi+1):
                if A[i] == target:
                    return i
            else:
                return -1
        mid_idx = (lo + hi) / 2
        mid_val = A[mid_idx]
        if mid_val > A[lo]:
            # left is normal
            if (mid_val >= target) and (A[lo] <= target):
                return self.norm_search(A, lo, mid_idx, target)
            return self.s_wrapper(A, mid_idx, hi, target)
        else:
            # right is normal
            if (mid_val <= target) and (A[hi] >= target):
                return self.norm_search(A, mid_idx, hi, target)
            return self.s_wrapper(A, 0, mid_idx, target)

    def norm_search(self, A, lo, hi, target):
        if (hi - lo) < 100:
            for i in range(lo, hi+1):
                if A[i] == target:
                    return i
            return -1
        mid_idx = (lo + hi) / 2
        mid_val = A[mid_idx]
        if mid_val == target:
            return mid_idx
        elif mid_val < target:
            return self.norm_search(A, mid_idx+1, hi, target)
        return self.norm_search(A, 0, mid_idx-1, target)

if __name__ == '__main__':
    s = Solution()
    print s.search(map(int, sys.argv[1].split(',')), int(sys.argv[2]))
