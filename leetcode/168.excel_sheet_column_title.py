#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param n, an integer
    # @return a string
    def convertToTitle(self, n):
        return self.c_wrapper(n, '')

    def c_wrapper(self, n, suffix):
        if n <= 0:
            return ''
        cl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        n -= 1
        remainder = (n % 26)
        quotient = n / 26
        s = '%s%s' % (cl[remainder], suffix)
        if quotient > 0:
            return self.c_wrapper(quotient, s)
        return s

if __name__ == '__main__':
    s = Solution()
    r = s.convertToTitle(int(sys.argv[1]))
    print r
