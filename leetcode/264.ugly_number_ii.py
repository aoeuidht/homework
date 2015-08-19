#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oj_helper import *

class Solution:
    def nthUglyNumber(self, n):
        if n < 2:
            return 1

        rst_list = [1]

        idxs = {2: 0, 3: 0, 5: 0}
        idxs = [0, 0, 0]
        for i in range(1, n):
            # find next
            c2 = rst_list[idxs[0]] * 2
            c3 = rst_list[idxs[1]] * 3
            c5 = rst_list[idxs[2]] * 5

            idx, val = 0, c2
            if c2 > c3:
                idx, val = 1, c3
            if val > c5:
                idx, val = 2, c5

            # append to rst tail and move the pivort
            rst_list.append(val)
            if c2 == val:
                idxs[0] += 1
            if c3 == val:
                idxs[1] += 1
            if c5 == val:
                idxs[2] += 1

            # for better memory performance
            idx = min(idxs)
            if idx > 100:
                rst_list[:100] = []
                idxs[0] -= 100
                idxs[1] -= 100
                idxs[2] -= 100

        return rst_list[-1]

if __name__ == '__main__':
    s = Solution()
    print s.nthUglyNumber(98)
    print s.nthUglyNumber(99)
    print s.nthUglyNumber(100)
    print s.nthUglyNumber(101)
    print s.nthUglyNumber(102)
    print s.nthUglyNumber(200)
