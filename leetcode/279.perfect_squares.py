#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from oj_helper import *


class Solution(object):
    def numSquares1(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = int(n ** 0.5)
        if n == (p * p):
            return 1

        cache = {0: 0,
                 1: 1}

        for i in xrange(2, n+1):
            p = int(i ** 0.5)
            if i == p * p:
                cache[i] = 1
                continue
            else:
                cache[i] = i

            for j in xrange(p, 0, -1):
                lookup = i - j * j
                tgt = cache[lookup] + 1
                if cache[i] > tgt:
                    cache[i] = tgt
                if cache[i] == 2:
                    break

        return cache[n]

    def numSquares(self, n):
        """

        Arguments:
        - `self`:
        - `n`:
        """
        cache = [n] * (n + 1)
        cache[0] = 0
        cache[1] = 1

        p = int(n ** 0.5)
        if p * p == n:
            return 1

        for i in range(0, n+1):
            for j in range(0, p+1):
                nxt = i + j * j
                if nxt > n:
                    break
                if cache[nxt] > cache[i] + 1:
                    cache[nxt] = cache[i] + 1
        return cache[n]



if __name__ == '__main__':
    s = Solution()
    print s.numSquares(8285)
    print s.numSquares(8829)
    """
    for x in range(1000):
        print x, s.numSquares(x)
    """
