#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        if not digits:
            return [1]
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            print i
            r = digits[i] + 1
            digits[i] = (r % 10)
            carry = r / 10
            if carry < 1:
                break
        return ([carry] + digits)  if (carry > 0) else digits

if __name__ == '__main__':
    s = Solution()
    v = lambda st: (st, s.plusOne(st))
    print v([0])
