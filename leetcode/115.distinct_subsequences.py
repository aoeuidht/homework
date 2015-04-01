#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        sl = len(S)
        tl = len(T)

        if tl > sl:
            return 0
        elif tl == sl:
            return 1 if (T == S) else 0
        if tl == 0:
            return 0
        # dp init
        dp = [0] * sl
        dp[0] = 1 if (S[0] == T[0]) else 0
        match = dp[0]
        for i in range(1, sl):
            if S[i] == T[0]:
                match += 1
            dp[i] = match

        print dp
        for i in range(1, tl):
            bk = dp[i]
            print dp, bk
            if S[i] == T[i]:
                dp[i] = 1 if dp[i-1] else 0
            else:
                dp[i] = 0
            dp[i-1] = 0
            for j in range(i+1, sl):
                if S[j] != T[i]:
                    bk, dp[j] = dp[j], dp[j-1]
                else:
                    bk, dp[j] = dp[j], bk+dp[j-1]
        print dp
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print s.numDistinct(* sys.argv[1:])
