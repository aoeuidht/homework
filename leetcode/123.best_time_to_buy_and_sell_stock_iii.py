#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        pl = len(prices)
        if pl < 2:
            return 0
        pro = [0] * (pl -1)
        for i in range(pl-1):
            pro[i] = prices[i+1] - prices[i]

        profit = 0
        start, end = -1, -1
        _p = 0
        _s = 0
        for idx, i in enumerate(pro):
            _p += i
            if _p > profit:
                profit = _p
                start, end = _s, idx
            if _p < 0:
                _p = 0
                _s = idx + 1
        if profit == 0:
            return 0

        loss = 0
        _l = 0
        for i in range(start, end+1):
            _l += pro[i]
            if _l < loss:
                loss = _l
            if _l > 0:
                _l = 0
            pro[i] = 0
        #print pro[start:end+1], start, end, profit, loss


        # the 2nd turn
        p2 = 0
        _p = 0
        for i in pro:
            _p += i
            if _p > p2:
                p2 = _p
            if _p < 0:
                _p = 0
        if (loss >= 0) or (-loss < p2):
            return profit + p2
        return profit - loss

if __name__ == '__main__':
    s = Solution()
    r = s.maxProfit(map(int, sys.argv[1:]))
    print r
