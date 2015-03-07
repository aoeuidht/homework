#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        sl = len(s) - 1
        start, end = 0, -1
        while sl >= 0:
            if ord(s[sl]) != 32:
                if end < 0:
                    end = sl
                start = sl
            else:
                if end >= 0:
                    break
            sl -= 1
        return end - start + 1

if __name__ == '__main__':
    s = Solution()
    v = lambda t: (t, s.lengthOfLastWord(t))
    print v('  ')
    print v(' ')
    print v('')
    print v('a')
    print v('  aa')
    print v(' aa ')
    print v('aa  ')
    print v(' aa  ')
