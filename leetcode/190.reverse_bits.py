#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return self.r_wrapper(n, 0, 0)

    def r_wrapper(self, n, r, c):
        if c == 32:
            return r
        l = n % 2
        return self.r_wrapper(n >> 1, (r << 1) + l, c+1)

if __name__ == '__main__':
    s = Solution()
    print s.reverseBits(int(sys.argv[1]))
