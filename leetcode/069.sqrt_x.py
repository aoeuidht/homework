#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x <= 0:
            return 0
        r = 1
        while True:
            rst = 0.5 * r + 0.5 * x / r
            print 0.5 * r, 0.5 * x / r
            print r, rst
            if abs(r - rst) < 1:
                return int(min(rst, r))
            r = rst

if __name__ == '__main__':
    s = Solution()
    print s.sqrt(int(sys.argv[1]))
