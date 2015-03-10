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

if __name__ == '__main__':
    s = Solution()
    v = lambda st: (st, s.isNumber(st))
    print v('hehehe')
