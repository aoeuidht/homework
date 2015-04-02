#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        rst = []
        if numRows > 0:
            rst.append([1])
        if numRows > 1:
            rst.append([1, 1])
        if numRows < 3:
            return rst
        for i in range(3, numRows+1):
            line = [1]
            for j in range(2, i):
                line.append(rst[-1][j-1] + rst[-1][j-2])
            line.append(1)
            rst.append(line)
        return rst

if __name__ == '__main__':
    s = Solution()
    r = s.generate(int(sys.argv[1]))
    for i in r:
        print i
