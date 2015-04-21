#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param numerator, an integer
    # @param denominator, an integern
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return '0'
        sign = 1
        if numerator < 0:
            sign *= -1
            numerator = -numerator
        if denominator < 0:
            sign *= -1
            denominator = -denominator

        rst = []

        remainder = numerator % denominator
        quotient = numerator / denominator

        rst.append((remainder, '%d' % quotient))
        rst_len = 1
        lo = None
        while remainder:
            diviend = 10 * remainder
            quotient = diviend / denominator
            r = (remainder, '%d' % quotient)
            remainder = diviend % denominator
            rst_len += 1
            rst.append(r)
            # look backward
            hi = rst_len-1
            for i in range(rst_len-1, 0, -1):
                if rst[i][0] == remainder:
                    lo = i
                    break
            if lo != None:
                break
        quotient = rst[0][1]

        if lo is None:
            if len(rst) > 1:
                __r =  '%s.%s' % (quotient, ''.join([i[1] for i in rst[1:]]))
            else:
                __r =  quotient
        else:
            _r = []
            for idx, v in enumerate(rst):
                if idx == lo:
                    _r.append('(')
                _r.append(v[1])
                if idx == 0:
                    _r.append('.')
                if idx == hi:
                    _r.append(')')
            __r = ''.join(_r)
        return __r if (sign > 0) else ('-%s' % __r)

if __name__ == '__main__':
    s = Solution()
    r = s.fractionToDecimal(*map(int, sys.argv[1:]))
    print r
