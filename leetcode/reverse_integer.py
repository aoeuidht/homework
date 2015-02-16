#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    def rwrapper(self, x, r):
        if x == 0:
            return r

        l = x % 10
        if r:
            rn = r * 10 + l
            if rn > 2147483647:
                return 0
            return self.rwrapper(x / 10, rn)
        return self.rwrapper(x / 10, l)

    # @return an integer
    def reverse(self, x):
        if x < 0:
            return -self.rwrapper(-x, 0)
        return self.rwrapper(x, 0)

if __name__ == '__main__':
    s = Solution()
    print s.reverse(int(sys.argv[1]))
