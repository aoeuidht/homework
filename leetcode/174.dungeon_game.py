#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from oj_helper import *

class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        if not dungeon:
            return 0

        rc, lc = len(dungeon), len(dungeon[0])
        dp = [1] * lc
        for ridx in range(rc-1, -1, -1):
            row = dungeon[ridx]
            dp[-1] = self.filter_rst((dp[-1] - row[-1],))
            for cidx in range(lc-2, -1, -1):
                cost = row[cidx]
                if ridx == (rc-1):
                    dp[cidx] = self.filter_rst((dp[cidx+1] - cost,))
                else:
                    dp[cidx] = self.filter_rst((dp[cidx] - cost,
                                                dp[cidx+1] - cost))
            print dp
        return dp[0]

    def filter_rst(self, cands):
        r = min(cands)
        return r if r > 0 else 1

if __name__ == '__main__':
    s = Solution()
    print s.calculateMinimumHP([[-2, -3, 3],
                                [-5, -10, 1],
                                [10, 30, -5]])
    print s.calculateMinimumHP([[-3, 5]])
    print s.calculateMinimumHP([[0, -3]])
    print s.calculateMinimumHP([[-3], [-7]])
    print s.calculateMinimumHP([[10,4,-48,-8,-87,9],[49,-100,6,-15,41,-99],[-76,-45,-26,50,46,14],[-81,-92,46,-62,-26,1],[-44,19,26,-98,-49,-72]])
