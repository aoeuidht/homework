#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if (not s) or (s[0] == '0'):
            return 0

        sl = len(s)
        idx = 0
        prev, cur = 1, 1
        while idx < (sl-1):
            print s[idx], prev, cur
            idx += 1
            v = int(s[idx-1:idx+1])
            c = int(s[idx])
            if c < 1:
                if (v < 1) or (v > 26):
                    return 0
                prev, cur = prev, prev
                continue
            if (0 < v < 27):
                if (v > c):
                    prev, cur = cur, cur + prev
                else:
                    prev, cur = cur, cur
            else:
                prev, cur = cur, cur
        return cur
if __name__ == '__main__':
    s = Solution()
    print s.numDecodings(sys.argv[1])
