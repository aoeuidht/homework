#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    def __init__(self):
        self.rst = []

    # @return a list of lists of integers
    def combine(self, n, k):
        cand = range(1, n+1)
        if n < k:
            return []
        elif n == k:
            return [cand]
        elif k == 1:
            return [[i] for i in cand]

        # the real part
        rst = []
        n += 1
        print range(1, n-k+1)
        for c in range(1, n-k+1):
            self.com_wrapper(n, k, [c], 1)
        return self.rst

    def com_wrapper(self, n, k, cand, cl):
        cmax = n - k + cl + 1
        ccur = cand[-1] + 1
        cl += 1
        cand.append(0)
        for i in range(ccur, cmax):
            cand[-1] = i
            if cl == k:
                self.rst.append(cand[:])
            else:
                self.com_wrapper(n, k, cand, cl)
        cand.pop()

if __name__ == '__main__':
    s = Solution()
    print s.combine(*map(int, sys.argv[1:]))
