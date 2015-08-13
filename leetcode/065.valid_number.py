#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        # resolve this by python, if u want to know the detail, just lookup
        # pystrtod.c, line 124 in the python source code.
        try:
            float(s)
            return True
        except:
            return False

    def isNumber1(self, s):
        s = s.strip()
        if not s:
            return False

        stat = 0
        i = 0
        j = len(s)
        c = s[i]
        if c in ('+', '-'):
            i += 1
            c = s[i]

        # 1123
        if '0' <= c <= '9':
            i += 1
            # loop until we met a non-digital number
            while (i < j) and ('0' <= s[i] <= '9'):
                i += 1
            if i >= j:
                return True
        elif c == '.':
            i += 1
            if i >= j:
                return False
            if not ('0' <= s[i] <= '9'):
                return False
            i -= 1
        else:
            return False

        # next should be . or eE
        if i >= j:
            return True

        c = s[i]
        if c == '.':
            i += 1
            while (i < j) and ('0' <= s[i] <= '9'):
                i += 1
            if i >= j:
                return True

        if s[i] not in ('e', 'E'):
            return False
        i += 1
        if i >= j:
            return False
        if s[i] in ('+', '-'):
            i += 1
        if i >= j:
            return False
        while (i < j) and ('0' <= s[i] <= '9'):
            i += 1
        if i >= j:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    scenarios = ['0.0',
                 '.0',
                 '00',
                 '01',
                 '1.2',
                 '2.3e0',
                 '2.0e',
                 '2.0e0',
                 '4e0',
                 '4e-0',
                 '-4e0',
                 '.0e45',
                 '3.',
                 '1 a ',
                 '01']


    v = lambda st: (st, s.isNumber1(st), s.isNumber(st))
    for r in map(v, scenarios):
        print r
