#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from oj_helper import *

def isBadVersion(ver):
    return ver > 5

class Solution:
    def firstBadVersion(self, n):
        s = 1
        e = n

        while s < e:
            if not isBadVersion(e):
                return e + 1

            mid = (e + s) // 2
            #print s, e, mid
            if mid == s:
                return s if isBadVersion(mid) else e

            if isBadVersion(mid):
                # on the left
                e = mid - 1
                continue
            else:
                s = mid + 1
                continue
        return s if isBadVersion(s) else (s + 1)

if __name__ == '__main__':
    s = Solution()

    isBadVersion = lambda x: x > 1
    print s.firstBadVersion(3)
    print s.firstBadVersion(2)
    print s.firstBadVersion(10)
    print s.firstBadVersion(1)
