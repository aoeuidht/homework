#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if (m < 2) or (n < 2):
            return 1
        dp = [1] * n
        print dp
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
            print dp
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print s.uniquePaths(*map(int, sys.argv[1:]))
