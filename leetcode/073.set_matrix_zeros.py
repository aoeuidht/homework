#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])

        memo = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # mark columns
                    for k in range(j, n):
                        if matrix[i][k] == 0:
                            memo[k] = 1
                    # clear line
                    for k in range(n):
                        matrix[i][k] = 0
                    break
        # set all columns

        print matrix, memo
        for i, v in enumerate(memo):
            print 'hehe', i, v
            if v == 1:
                for j in range(m):
                    matrix[j][i] = 0
        for i in matrix:
            print i

if __name__ == '__main__':
    s = Solution()
    print s.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])
