#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from oj_helper import *

class Solution:
    # @return an integer as the maximum profit
    def maxProfit(self, k, prices):
        if len(prices) < 2:
            return 0
        _profits = [prices[i+1] - prices[i]
                    for i in range(len(prices) - 1)]
        # merge the profits
        profits = []
        sign = None
        for p in _profits:
            if p == 0:
                continue
            if sign == (p > 0):
                profits[-1] += p
            else:
                profits.append(p)
                if sign is None:
                    sign = (p > 0)
                else:
                    sign = not sign
        if not profits:
            return 0
        lo = 0 if (profits[0] > 0) else 1
        hi = (len(profits)-1) if (profits[-1] > 0) else (len(profits)-2)
        cands = profits[lo:hi+1]
        print cands, profits, _profits
        print lo, hi, profits,range((hi-lo)/2, k-1, -1)
        for i in range((hi-lo)/2, k-1, -1):
            self.eat_one(cands)
        rst = 0
        print cands
        for i in cands:
            rst += (i if i > 0 else 0)
        return rst


    def eat_one(self, cands):
        cl = len(cands)
        max_idx, max_val = 1, cands[1]
        for idx in range(3, cl, 2):
            v = cands[idx]
            if v > max_val:
                max_idx, max_val = idx, v
        # eat the two neighbor
        min_idx, min_val = 0, cands[0]
        print cl, cands
        for idx in range(2, cl+1, 2):
            print idx
            v = cands[idx]
            if v < min_val:
                min_idx, min_val = idx, v
        # we skip, or we merge
        # operation on the negative ones
        if min_val + max_val >= 0:
            cands[max_idx-1:max_idx+2] = [sum(cands[max_idx-1:max_idx+2])]
        else:
            if min_idx == 0:
                cands[0:2] = []
            elif min_idx == (cl-1):
                cands[-2:] = []
            else:
                cands[min_idx-1:min_idx+2] = [sum(cands[min_idx-1:min_idx+2])]


if __name__ == '__main__':
    s = Solution()
    # 2 8,6,4,3,3,2,3,5,8,3,8,2,6
    print s.maxProfit(int(sys.argv[1]),
                      map(int, sys.argv[2].split(',')))
