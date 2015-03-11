#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        rst = []
        al, bl = len(a), len(b)
        print a, b, al, bl
        to_int = lambda(s): map(int, list(s)[::-1])
        if al > bl:
            l, ll = to_int(a), al
            s, sl = to_int(b), bl
        else:
            l, ll = to_int(b), bl
            s, sl = to_int(a), al
        carry = 0
        for i in range(ll):
            lv = l[i]
            sv = 0 if (i >= sl) else s[i]
            r = lv + sv + carry
            rst.append(str(r % 2))
            carry = r / 2
        if carry > 0:
            rst.append('1')
        print rst
        return ''.join(rst[::-1])

if __name__ == '__main__':
    s = Solution()
    print s.addBinary(*sys.argv[1:])
