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
        if nl == 1:
            return num[0]
        # if we robber the house
        dp_r = [0] * nl
        # if the house is safe
        dp_s = [0] * nl

        # what happens if we skip the 1st one
        dp_s1 = [0] * nl
        dp_r1 = [0] * nl

        for idx, v in enumerate(num):
            if idx == 0:
                dp_r[idx] = v
                continue
            dp_s[idx] = max(dp_r[idx-1], dp_s[idx-1])
            dp_r[idx] = dp_s[idx-1] + v

            dp_s1[idx] = max(dp_r1[idx-1], dp_s1[idx-1])
            dp_r1[idx] = dp_s1[idx-1] + v
        print 'robber', dp_r
        print 'skip', dp_s
        print 'skip-1-robber', dp_r1
        print 'skip-1-skip', dp_s1
        return max(dp_s[-1], dp_r[-2], dp_s1[-1], dp_r1[-1])

if __name__ == '__main__':
    s = Solution()
    print s.rob(map(int, sys.argv[1].split(',')))
