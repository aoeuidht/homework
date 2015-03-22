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
        print A[lo:hi+1]
        if (hi - lo) < 5:
            for i in range(lo, hi+1):
                if A[i] == target:
                    return i
            else:
                return -1
        mid_idx = (lo + hi) / 2
        mid_val = A[mid_idx]
        if mid_val == target:
            return mid_idx
        if A[lo] == A[hi]:
            lr = self.s_wrapper(A, lo, mid_idx-1, target)
            rr = self.s_wrapper(A, mid_idx + 1, hi, target)
            if (lr == -1) and (rr == -1):
                return -1
            return 1
        elif A[lo] < A[hi]:
            return self.norm_search(A, lo, hi, target)

        # now we handle the reverse list
        if mid_val == A[lo]:
            # right
            return self.s_wrapper(A, mid_idx + 1, hi, target)
        if mid_val == A[hi]:
            # left
            return self.norm_search(A, lo, hi, target)
        # the original case
        if mid_val > A[lo]:
            # left is normal
            if (mid_val >= target) and (A[lo] <= target):
                return self.norm_search(A, lo, mid_idx+1, target)
            return self.s_wrapper(A, mid_idx+1, hi, target)
        else:
            # right is normal
            if (mid_val <= target) and (A[hi] >= target):
                return self.norm_search(A, mid_idx+1, hi, target)
            return self.s_wrapper(A, lo, mid_idx+1, target)

    def norm_search(self, A, lo, hi, target):
        print A[lo:hi+1], target
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
    v = lambda x, y: (y, s.search(x, y))
    """
    print v([1, 1, 1, 1, 1, 1], 2)
    print v([1, 1, 1, 1, 1, 1, 2, 2], 2)
    print v([1, 1, 1, 1, 1, 1, 2, 2], 2)
    print v([1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1], 2)
    print v([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1], 2)
    print v([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1], 2)
    print v([100] * 10 + range(101, 200) + range(1, 80) + [80] * 10,
            100)
    print v([100] * 10 + range(101, 181) + range(1, 50) + [80] * 10,
            100)
    print v([100] * 10 + range(101, 200) + range(1, 80) + [80] * 10,
            110)
    print v([100] * 10 + range(101, 200) + range(1, 80) + [80] * 10,
            50)
    print v([100] * 10 + range(101, 200) + range(1, 80) + [80] * 10,
            199)
    """
    print v([1,2,2,2,0,1,1], 0)
