#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        l1, l2 = len(num1), len(num2)
        if l1 > l2:
            sl,ss = num1, num2
        else:
            sl, ss = num2, num1
        r = []
        multiplicand = map(int, list(sl)[::-1])
        for times, i in enumerate(list(ss)[::-1]):
            _r = self.string_mul_char(multiplicand, i, times)
            r = self.string_add(r, _r)
        rst = ''.join(map(lambda i: chr(48+i), r[::-1]))
        return rst if rst else '0'

    def string_add(self, l, r):
        ll, rl = len(l), len(r)
        e = 0
        if ll > rl:
            llist, slist = l, r
            llen, slen = ll, rl
        else:
            slist, llist = l, r
            llen, slen = rl, ll
        rst = []
        for i in range(slen):
            _r = llist[i] + slist[i] + e
            rst.append(_r % 10)
            e = _r / 10

        for i in range(slen, llen):
            if e == 0:
                rst += llist[i:]
                break
            _r = llist[i] + e
            rst.append(_r % 10)
            e = _r / 10
        if e:
            rst.append(e)
        return rst

    def string_mul_char(self, multiplicand, multiplier, times):
        e = 0
        c = int(multiplier)
        if c == 0:
            return []
        rst = []
        for v in multiplicand:
            r = v * c + e
            rst.append(r%10)
            e = r / 10
        if e:
            rst.append(e)
        # take care! its the reverse order
        return [0] * times + rst

if __name__ == '__main__':
    s = Solution()
    print s.multiply(*sys.argv[1:])
