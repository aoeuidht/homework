#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    def titleToNumber(self, s):
        rst = 0
        _c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        cd = dict(zip(_c, range(1, 27)))
        for c in s:
            rst *= 26
            rst += cd[c]
        return rst

if __name__ == '__main__':
    s = Solution()
    r = s.titleToNumber(sys.argv[1])
    print r
