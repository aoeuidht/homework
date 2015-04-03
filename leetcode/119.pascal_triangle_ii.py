#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @return a list of lists of integers
    def generate(self, rowIndex):
        numRows = rowIndex
        rst = [[1], [1, 1]]
        if numRows < 2:
            return rst[numRows]
        prev = rst[-1]
        for i in range(2, numRows+1):
            print i
            line = [1]
            for j in range(2, i+1):
                line.append(prev[j-1] + prev[j-2])
            line.append(1)
            prev = line[:]

        return line

if __name__ == '__main__':
    s = Solution()
    print s.generate(int(sys.argv[1]))
