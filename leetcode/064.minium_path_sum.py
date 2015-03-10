#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        if n < 1:
            return 0
        dp = [-1] * n
        dp[0] = 0
        for i in range(0, m):
            dp[0] += grid[i][0]
            print 'line 22', dp, i
            for j in range(1, n):
                if dp[j] < 0:
                    dp[j] = dp[j-1] + grid[i][j]
                    print 'continue here', dp
                    continue
                print dp
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
                print dp
        return dp[-1]

        return 0

if __name__ == '__main__':
    s = Solution()
    print s.minPathSum([[1,2,3,4,5]])
    print s.minPathSum([[0]])
    print s.minPathSum([[]])
    print s.minPathSum([[0,1],[1,0]])
