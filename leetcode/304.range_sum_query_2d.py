#!/usr/bin/env python
# -*- coding: utf-8 -*-

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.h = len(matrix)

        if self.h:
            self.w = len(matrix[0])
            self.m = [[0] * (self.w + 1)]
            for i in range(self.h):
                prev_line = self.m[-1][:]
                line = [0] * (self.w + 1)
                for j in range(self.w):
                    line[j+1] = line[j] + matrix[i][j]
                newline = map(sum, zip(prev_line, line))
                self.m.append(newline)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if (row2 >= self.h) or (col2 >= self.w):
            return 0
        if (col1 < 0) or (row1 < 0):
            return 0

        print (self.m[row2 + 1][col2 + 1],
                self.m[row1][col1],
                self.m[row1][col2+1],
                self.m[row2+1][col1])

        return (self.m[row2 + 1][col2 + 1] +
                self.m[row1][col1] -
                self.m[row1][col2+1] -
                self.m[row2+1][col1])


matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]
numMatrix = NumMatrix(matrix)
for a in numMatrix.m:
    print a
print numMatrix.sumRegion(2, 1, 4, 3)
print numMatrix.sumRegion(1, 1, 2, 2)
print numMatrix.sumRegion(1, 2, 2, 4)
print numMatrix.sumRegion(1, 2, 2, 40)
