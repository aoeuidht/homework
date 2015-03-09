#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @return an integer
    def uniquePaths(self, obstacleGrid):
        if not obstacleGrid:
            return 1
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1
        for i in range(0, m):
            dp[0] = 1 if (obstacleGrid[i][0] == 0) and (dp[0] > 0) else 0
            for j in range(1, n):
                if obstacleGrid[i][j] < 1:
                    dp[j] += dp[j-1]
                else:
                    dp[j] = 0
            print dp
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print s.uniquePaths([[0]])
