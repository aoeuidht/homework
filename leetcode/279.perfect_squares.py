#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from oj_helper import *


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = n ** 0.5
        if n == (p ** 2):
            return 1
        cache = {0: 0,
                 1: 1}
        for i in range(2, n+1):
            cache[i] = i
            for j in range(1, int(i ** 0.5) + 1):
                lookup = i - j ** 2
                if lookup:
                    cache[i] = min(cache[i],
                                   cache[i - j **2] + 1)
                else:
                    cache[i] = 1
                    break

        return cache[n]


if __name__ == '__main__':
    s = Solution()
    print s.numSquares(8285)
