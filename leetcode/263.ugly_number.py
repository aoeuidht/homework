#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oj_helper import *

class Solution:
    def isUgly(self, num):
        if num < 1:
            return False
        while True:
            ugly = True
            o = num
            for d in (2, 3, 5):
                if (num % d):
                    continue
                num /= d
            ugly = (num == o)
            if ugly:
                break
        if num > 1:
            return False
        return True

if __name__ == '__main__':
    s = Solution()
    print s.isUgly(1)
    print s.isUgly(2)
    print s.isUgly(3)
    print s.isUgly(5)
    print s.isUgly(6)
    print s.isUgly(8)
    print s.isUgly(14)
    print s.isUgly(-2147483648)
    print s.isUgly(2147483648)
