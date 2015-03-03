#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix[0])
        for i in range(n/2 + 1):
            self.r_wrapper(matrix, n, i)
        return matrix

    def r_wrapper(self, num, n, offset):
        i = offset
        hi = n - i - 1
        for j in range(i, hi):
            # rotate from (n, n) to (n, hi-1)
            t = num[i][j]
            num[i][j] = num[n-1-j][i]
            num[n-1-j][i] = num[n-1-i][n-1-j]
            num[n-1-i][n-1-j] = num[j][n-1-i]
            num[j][n-1-i] = t




if __name__ == '__main__':
    s = Solution()
    print s.rotate([[1, 2], [3,4]])
    #print s.permuteUnique(map(int, sys.argv[1].split(',')))
