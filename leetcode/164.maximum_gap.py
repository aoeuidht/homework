#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from oj_helper import *

class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        nl = len(num)
        if nl < 2:
            return 0

        bsize = 256
        boffset = 24
        buckets = [[] for i in range(bsize)]

        for i in num:
            bidx = i >> boffset
            buckets[bidx].append(i)
        for i in range(bsize):
            buckets[i].sort()

        # do the count
        prev = None
        rst = 0
        for bucket in buckets:
            if not bucket:
                continue
            bl = len(bucket)
            for v in bucket:
                if prev == None:
                    prev = v
                    continue
                g = v - prev
                rst = g if g > rst else rst
                prev = v

        return rst

if __name__ == '__main__':
    s = Solution()
    print s.maximumGap(map(int, sys.argv[1].split(',')))
