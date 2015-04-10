#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    def minCut(self, s):
        if not s:
            return 0
        # I got the amazing algorithm at
        # https://leetcode.com/discuss/9476/solution-does-not-need-table-palindrome-right-uses-only-space
        n = len(s)
        dp = range(-1, n)
        print dp
        for i in range(n):
            for j in range(i+1):
                if (((i+j) < n) and
                    (s[i-j] == s[i+j])):
                    dp[i+j+1] = min(dp[i+j+1], dp[i-j]+1)
                else:
                    break
            for j in range(1, i+2):
                if (((i+j) < n) and
                    (s[i-j+1] == s[i+j])):
                    dp[i+j+1] = min(dp[i+j+1], dp[i-j+1]+1)
                else:
                    break
        print dp
        return dp[n] + 1

if __name__ == '__main__':
    s = Solution()
    r = s.minCut(sys.argv[1])
    print r
