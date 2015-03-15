#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):

        rst = 0
        pairs_most = (n / 2) + (n % 2)
        for num in range(pairs_most, n+1):
            pair_num = n - num
            single_num = num * 2 - n
            print 'pair', pair_num, ' single', single_num
            # only the math
            r = self.combina(max(pair_num, single_num)+1,
                             min(pair_num, single_num))
            print pair_num, single_num, r
            rst += r
        return rst

    def combina(self, m, n):
        print m, n
        if n == 0:
            return 1
        elif n == 1:
            return m
        dp = range(1, m+1)
        for i in range(1, n):
            for j in range(1, m):
                dp[j] += dp[j-1]
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print s.climbStairs(int(sys.argv[1]))
