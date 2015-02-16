#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""
class Solution:
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s
        ss = ['#'] * (len(s) * 2 + 1)
        p = [0] * len(ss)
        for i in xrange(len(s)):
            ss[i*2+1] = s[i]
            p[i*2+1] = 1

        pcen, ptail = 1, 2
        h, t = -1, len(ss)
        for i in xrange(2, len(ss)):
            if ptail >= i:
                p[i] = p[2*pcen-i] if (p[2*pcen-i] < (ptail -i)) else (ptail - i)
            while ((i - p[i]) > h) and ((i + p[i]) < t) and (ss[p[i]+i] == ss[i-p[i]]):
                p[i] += 1
            if (i + p[i]) > ptail:
                ptail = i + p[i]
                pcen = i

        pcen, plen = 0, 1
        for _c, _l in enumerate(p):
            if _l > plen:
                pcen, plen = _c, _l
        rlen = 2 * plen - 1
        rs = pcen - plen + 1
        return ''.join([ss[rs+i] for i in range(1, rlen) if i % 2])

if __name__ == '__main__':
    s = Solution()
    with open('longest_palindromic_substring.data') as f:
        for i in range(int(sys.argv[1])):
            f.readline()
        ss = f.readline()
        f.close()
    print ss
    print s.longestPalindrome(ss[:-1])
