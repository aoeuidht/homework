#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        rst = 0
        while n:
            n /= 5
            rst += n
        return rst


if __name__ == '__main__':
    s = Solution()
    r = s.trailingZeroes(int(sys.argv[1]))
    print r
