#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from oj_helper import *


class Solution(object):

    def n_wrapper(self, n, cache):
        if cache.has_key(n):
            return cache[n]

        # find the minium
        p = int(n ** 0.5)
        # is it the square of 1
        if p * p == n:
            return 1
        # is it the square of 2
        for i in range(p, 0, -1):
            val = i * i
            n_left = n - val
            # is n_left square root
            ns = int(n_left ** 0.5)
            if ns * ns == n_left:
                cache[n] = 2
                return 2

        # bigger than 2
        n_left = n
        rst_min = n
        for i in range(p, 0, -1):
            val = i * i
            cache[val] = 1
            if val < n:
                n_left = n - val
                if cache.has_key(n_left):
                    _rst = cache[n_left] + 1
                else:
                    _rst = 1 + self.n_wrapper(n_left, cache)
                rst_min = min(_rst, rst_min)
                if rst_min <= 3:
                    break
        cache[n] = rst_min
        return rst_min

    def numSquares(self, n):
        """

        Arguments:
        - `self`:
        - `n`:
        """
        cache = {0: 0,
                 1: 1}

        rst = self.n_wrapper(n, cache)
        print n, len(cache), rst
        return rst



if __name__ == '__main__':
    s = Solution()
    print s.numSquares(8285)
    print s.numSquares(8829)
    print s.numSquares(5756)
    print s.numSquares(12)
    """
    for x in range(1000):
        print x, s.numSquares(x)
    """
