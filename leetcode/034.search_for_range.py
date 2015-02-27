#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        return self.s_wrapper(A, 0, len(A)-1, target)

    def s_wrapper(self, A, lo, hi, tgt):
        r = [-1, -1]
        if (hi - lo) < 100:
            for i in range(lo, hi+1):
                if A[i] == tgt:
                    if r[0] < 0:
                        r[0] = i
                    else:
                        r[1] = i
            if (r[0] > -1) and (r[1] == -1):
                r[1] = r[0]
            return r
        mid_idx = (lo + hi) / 2
        mid_val = A[mid_idx]
        if mid_val > tgt:
            # in left
            return self.s_wrapper(A, lo, mid_idx-1, tgt)
        elif mid_val < tgt:
            return self.s_wrapper(A, mid_idx+1, hi, tgt)
        # met the mid
        lr = self.s_wrapper(A, lo, mid_idx, tgt)
        rr = self.s_wrapper(A, mid_idx, hi, tgt)
        return [lr[0], rr[1]]

if __name__ == '__main__':
    s = Solution()
    print s.searchRange(map(int, sys.argv[1].split(',')), int(sys.argv[2]))
