#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        if n < 1:
            return 0
        r = 0
        while n:
            if n < 10:
                r += 1
                break

            b = self.get_b(n)
            bc = self.get_cnt_by_batch(b)
            i = int(n / b)
            n = n % b

            if i == 1:
                r += bc + 1 + n
            else:
                r += b + i * bc
        return r


    def get_b(self, n):
        b = 1
        while n:
            b += 1
            n = int(n / 10)
        return 10 ** (b - 2)

    def get_cnt_by_batch(self, b):
        _b, r = 10, 1
        while (_b < b):
            r = _b + 10 * r
            _b *= 10
        return r

def cnt(num):
    """

    Arguments:
    - `num`:
    """
    calc = lambda items: len([i for i in str(items) if i == '1'])
    return sum(map(calc, range(1, num+1)))

if __name__ == '__main__':

    s = Solution()
    for i in range(2000):
        print i, cnt(i), s.countDigitOne(i)

    """
    _b = lambda x: (x, s.get_b(x), s.get_cnt_by_batch(s.get_b(x)))
    print _b(0)
    print _b(1)
    print _b(9)
    print _b(10)
    print _b(11)
    print _b(99)
    print _b(100)
    print _b(900)
    print _b(1000)
    """
