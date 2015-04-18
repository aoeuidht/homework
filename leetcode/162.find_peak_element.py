#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from oj_helper import *

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, num):
        bl = True
        for k in range(0, len(num)-1):
            if bl and (num[k] > num[k+1]):
                return k
                bl = num[k] < num[k+1]
        return len(num) -1
        # I still don't understand this question
        # https://leetcode.com/discuss/28285/a-relative-concise-python-code
        l,r = 0,len(num)-1
        while l < r:
            if (r - l) < 30:
                bl = True
                for k in range(l, r):
                    if bl and (num[k] > num[k+1]):
                        return k
                    bl = num[k] < num[k+1]
                return r

            mid = (l+r)/2
            if num[mid] < num[mid+1]:
                l = mid+1
            elif num[mid] > num[mid+1]:
                r = mid
        return r

if __name__ == '__main__':
    s = Solution()
    print s.findPeakElement(map(int, sys.argv[1].split(',')))
