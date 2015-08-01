#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from oj_helper import *

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if (not matrix) or (not matrix[0]):
            return False

        w, h = len(matrix[0]), len(matrix)
        return self.s_wrapper(matrix, target, 0, w, 0, h)

    def s_wrapper(self, matrix, target, w0, w1, h0, h1):
        if (w0 >= w1) or (h0 >= h1):
            return False
        offset = 0

        while (w0 + offset < w1) and (h0 + offset < h1):
            v = matrix[h0+offset][w0+offset]
            if v == target:
                return True
            if v > target:
                break
            offset += 1
        if offset < 1:
            return False

        # the left
        return (self.s_wrapper(matrix, target, w0, w0+offset,
                               h0+offset, h1) or
                self.s_wrapper(matrix, target, w0+offset, w1,
                               h0, h0+offset))


if __name__ == '__main__':
    s = Solution()
    matrix = [[48,65,70,113,133,163,170,216,298,389],
              [89,169,215,222,250,348,379,426,469,554],
              [178,202,253,294,367,392,428,434,499,651],
              [257,276,284,332,380,470,516,561,657,698],
              [275,331,391,432,500,595,602,673,758,783],
              [357,365,412,450,556,642,690,752,801,887],
              [359,451,534,609,654,662,693,766,803,964],
              [390,484,614,669,684,711,767,804,857,1055],
              [400,515,683,732,812,834,880,930,1012,1130],
              [480,538,695,751,864,939,966,1027,1089,1224]]
    print s.searchMatrix(matrix, int(sys.argv[1]))
    for l in matrix:
        print l
