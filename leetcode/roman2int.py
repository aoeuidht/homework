#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution:

    def token_to_val(self, t):
        """ token to magnitude"""
        rst = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
        return rst[t]

    def romanToInt(self, s):
        sl = len(s)
        c = 0
        prev_val = 0
        rst = 0

        for c in s:
            val = self.token_to_val(c)
            if prev_val >= val:
                rst += val
            else:
                rst += (val - prev_val * 2)
            prev_val = val
        return rst

if __name__ == '__main__':
    s = Solution()
    print s.romanToInt(sys.argv[1])
