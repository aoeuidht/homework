#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        # I got the idea at ``https://web.stanford.edu/class/cs124/lec/med.pdf''
        m, n = len(word1), len(word2)
        dp = range(n+1)
        print dp
        for i in range(1, m+1):
            for j in range(n+1):
                if j == 0:
                    dp_ij = dp[0]
                    dp[0] = i
                    continue

                dp_ij_bak = dp[j]
                dp[j] = min(dp[j-1] + 1,
                            dp[j] + 1,
                            dp_ij + (0 if (word1[i-1] == word2[j-1]) else 1))
                dp_ij = dp_ij_bak
            print dp
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print s.minDistance(*sys.argv[1:])
