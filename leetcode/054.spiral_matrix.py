#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        for i in matrix:
            print i
        if not matrix:
            return []
        r = []
        xl, xh, yl, yh = 0, len(matrix)-1, 0, len(matrix[0])-1
        while (xl <= xh) and (yl <= yh):
            #print xl, xh, yl, yh
            if xl == xh:
                r += [matrix[xl][i] for i in range(yl, yh+1)]
                break
            if yl == yh:
                r += [matrix[i][yl] for i in range(xl, xh+1)]
                break


            # (xl, yl) -> (xl, yh)
            r += [matrix[xl][i] for i in range(yl, yh)]
            # (xl, yh) -> (xh, yh)
            r += [matrix[i][yh] for i in range(xl, xh)]
            # (xh, yh) -> (xh, yl)
            r += [matrix[xh][i] for i in range(yh, yl, -1)]
            # (xh, yl) -> (xl, yl)
            r += [matrix[i][yl] for i in range(xh, xl, -1)]
            xl, xh, yl, yh = xl+1, xh-1, yl+1, yh-1
        return r

if __name__ == '__main__':
    s = Solution()
    i, j = map(int, sys.argv[1:3])
    p = []
    for x in range(j):
        p.append(range(x*i, x*i+i))
    print s.spiralOrder(p)
