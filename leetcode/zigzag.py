#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @return a string
    def convert(self, s, nRows):
        glen = nRows * 2 - 2
        if glen < 2:
            return s
        slen = len(s)
        gnum = (slen-1) / glen  + 1
        rst = [''] * slen
        piv = 0
        # low
        for i in range(nRows):
            # columns
            for offset in range(gnum):
                idx = offset * glen + i
                if idx < slen:
                    rst[piv] = s[idx]
                    piv += 1
                # another to add
                if 0 < i < (nRows - 1):
                    idx = offset * glen + glen - i
                    if idx < slen:
                        rst[piv] = s[idx]
                        piv += 1
        return ''.join(rst)

if __name__ == '__main__':
    s = Solution()
    with open('zigzag.txt') as f:
        for i in range(int(sys.argv[1])):
            f.readline()
        ss = f.readline()
        f.close()
    print ss
    print s.convert(ss[:-1], 3)
