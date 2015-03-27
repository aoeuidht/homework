#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        ls1, ls2, ls3 = map(len, (s1, s2, s3))
        if (ls1 + ls2) != ls3:
            return False
        if ls1 == 0:
            return s2 == s3
        if ls2 == 0:
            return s1 == s3

        dp = [-1] * (ls1 + 1)

        #init the dp
        dp[0] = 0
        for j in range(1, ls1+1):
            if s3[j-1] == s1[j-1]:
                dp[j] = j - 1
            else:
                break
        for i in range(0, ls2):
            dp[0] = (-1 if (dp[0] == -1) else
                     (i if (s2[i] == s3[i]) else -1))
            # move down
            for j in range(1, ls1+1):
                if dp[j] > -1:
                    if s3[dp[j]+1] == s2[i]:
                        dp[j] += 1
                    else:
                        dp[j] = -1

            # go right
            for j in range(0, ls1):
                if dp[j] > -1:
                    if s3[dp[j]+1] == s1[j]:
                        dp[j+1] = dp[j] + 1

        return dp[-1] > -1

if __name__ == '__main__':
    s = Solution()
    print s.isInterleave(*sys.argv[1:])
