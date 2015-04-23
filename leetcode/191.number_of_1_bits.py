#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        r = 0
        for i in xrange(32):
            if n == 0:
                break
            if n % 2:
                r += 1
            n = n >> 1
        return r


if __name__ == '__main__':
    s = Solution()
    print s.hammingWeight(int(sys.argv[1]))
