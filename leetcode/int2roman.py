#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""Given an integer,  convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution:
    def get_magnitude(self, num):
        m = 1
        while num > 9:
            m *= 10
            num /= 10
        return m

    def get_magn_token(self, magn):
        rst = {1: 'I',
               10: 'X',
               100: 'C',
               1000: 'M'}
        return rst[magn]

    def get_magnh_token(self, magn):
        rst = {1: 'V',
               10: 'L',
               100: 'D'}
        return rst[magn]

    def get_magnp_token(self, magn):
        rst = {1: 'X',
               10: 'C',
               100: 'M'}
        return rst[magn]

    # @return a string
    def intToRoman(self, num):
        if (num > 3999) or (num < 1):
            return ''
        rst = []
        while num > 0:
            m = self.get_magnitude(num)
            b = num / m
            print num, m, b
            if b == 9:
                rst.append(self.get_magn_token(m))
                rst.append(self.get_magnp_token(m))
            elif b > 4:
                rst.append(self.get_magnh_token(m))
                for _i in range(b-5):
                    rst.append(self.get_magn_token(m))
            elif b == 4:
                rst.append(self.get_magn_token(m))
                rst.append(self.get_magnh_token(m))
            else:
                for _i in range(b):
                    rst.append(self.get_magn_token(m))
            num = num % m
        return ''.join(rst)

if __name__ == '__main__':
    s = Solution()
    print s.intToRoman(int(sys.argv[1]))
