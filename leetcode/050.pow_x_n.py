#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n < 0:
            return 1 / self.pow(x, -n)
        elif n == 0:
            return 1
        elif n == 1:
            return x

        r = self.pow(x, n/2)
        if n % 2:
            return r * r *x
        return r * r


if __name__ == '__main__':
    s = Solution()
    print s.pow(float(sys.argv[1]), int(sys.argv[2]))
