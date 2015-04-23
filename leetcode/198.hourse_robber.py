#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if not num:
            return 0
        nl = len(num)
        # if we robber the house
        dp_r = [0] * nl
        # if the house is safe
        dp_s = [0] * nl

        for idx, v in enumerate(num):
            if idx == 0:
                dp_r[idx] = v
                continue
            dp_s[idx] = max(dp_r[idx-1], dp_s[idx-1])
            dp_r[idx] = dp_s[idx-1] + v
        print dp_r
        print dp_s
        return max(dp_s[-1], dp_r[-1])

if __name__ == '__main__':
    s = Solution()
    print s.rob(map(int, sys.argv[1].split(',')))
