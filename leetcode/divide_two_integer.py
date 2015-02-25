#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
class Solution:
    def abs(self, v):
        return (1, v) if (v > 0) else (-1, -v)

    def filter_rst(self, r):
        if r > 0:
            return r if (r < 2147483647) else 2147483647
        else:
            return r if (r > -2147483648) else -2147483648

    # @return an integer
    def divide(self, dividend, divisor):
        sdend, dividend = self.abs(dividend)
        sdsor, divisor = self.abs(divisor)

        if (divisor & (divisor -1)) == 0:
            while divisor > 1:
                divisor >>= 1
                dividend >>= 1
            return self.filter_rst(sdend * sdsor * dividend)
        else:
            r = 0
            while dividend >= divisor:
                _dsor, mult = divisor, 1
                while dividend >= _dsor:
                    r += mult
                    dividend -= _dsor
                    # now multiple the _dsor
                    _dsor <<= 1
                    mult <<= 1
            print r
            r = r * sdend * sdsor
            return self.filter_rst(r)

if __name__ == '__main__':
    s = Solution()
    print s.divide(*map(int, sys.argv[1:]))
