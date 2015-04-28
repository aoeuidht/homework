#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        rst = False
        his = set()
        r = n
        while True:
            r = self.square_sum(r)
            if r == 1:
                rst = True
                break
            if r in his:
                break
            his.add(r)
        return rst

    def square_sum(self, n):
        if n < 0:
            return -1
        r = 0
        while n > 0:
            r += ((n % 10) ** 2)
            n /= 10
        return r

if __name__ == '__main__':
    s = Solution()
    print s.isHappy(int(sys.argv[1]))
