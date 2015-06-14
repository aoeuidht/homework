#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        h = len(matrix)
        if h == 1:
            l = map(int, list(matrix[0]))
            return 1 if any(l) else 0

        rst = 0
        w = len(matrix[0])
        # how many 1s on top
        con_h = [0] * w

        # how many 1s on left
        con_w = [0] * w
        con_s = [0] * w
        for ls in matrix:
            l = map(int, list(ls))
            con_h[0] = l[0]
            con_w[0] = l[0]
            rst_left_top = con_s[0]
            con_s[0] = l[0]
            for idx in range(1, w):
                con_h[idx] = (con_h[idx] + 1) if l[idx] else 0
                con_w[idx] = (con_w[idx-1] + 1) if l[idx] else 0
                rst_bk = con_s[idx]
                con_s[idx] = (min(con_h[idx], con_w[idx], rst_left_top + 1)
                              if l[idx] else 0)
                rst_left_top = rst_bk
            rst = max(rst, max(con_s))
            print l, con_h, con_w, con_s
        return rst

if __name__ == '__main__':
    s = Solution()
    print s.maximalSquare([[1, 0, 1, 0, 0],
                           [1, 0, 1, 1, 1],
                           [1, 1, 1, 1, 1],
                           [1, 0, 0, 1, 0]])

    print s.maximalSquare(["0"])
    print s.maximalSquare(["11111111","11111110","11111110","11111000","01111000"])
