#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @return an integer
    def numTrees(self, n):
        _r = [0, 1, 2, 5]
        if n < 4:
            return _r[n]

        _r[0] = 1
        _r += [0] * (n - 3)

        for i in range(4, n+1):
            self.calc_num(_r, i)
        print _r
        return _r[-1]

    def calc_num(self, rst, idx):
        c = 0
        for i in range(0, idx):
            c += rst[i] * rst[idx-1-i]
        rst[idx] = c


if __name__ == '__main__':
    s = Solution()
    print s.numTrees(int(sys.argv[1]))
