#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        mem = {}
        cn = 0
        for idx, i in enumerate(num):
            if mem.has_key(i):
                continue
            mem[i] = i
            il, ih = i-1, i+1
            l = mem.get(il, i)
            r = mem.get(ih, i)
            mem[r], mem[l] = l, r
            cn = max(cn, r - l + 1)
        return cn

if __name__ == '__main__':
    s = Solution()
    r = s.longestConsecutive([100, 4, 200, 1, 3, 2])
    print r
    r = s.longestConsecutive([-1, 1, 0])
    print r
    r = s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
    print r
