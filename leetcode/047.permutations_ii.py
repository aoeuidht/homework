#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num.sort()
        rst = []
        nl = len(num)
        if nl < 2:
            return [num]

        self.p_wrapper(num, 0, nl-1, rst)
        return rst

    def p_wrapper(self, num, lo, hi, rst):
        if lo > hi:
            return
        elif lo == hi:
            rst.append(num[:])
        l = num[lo]
        for i in range(lo, hi+1):
            if (l == num[i]):
                if i == lo:
                    self.p_wrapper(num, lo+1, hi, rst)
                n = num[:]
                for j in range(i+1, hi+1):
                    if num[j] == l:
                        continue
                    n[:lo] = num[:lo]
                    n[lo] = num[j]
                    n[lo+1:j+1] = num[lo:j]
                    self.p_wrapper(n, lo+1, hi, rst)
                break
            else:
                num[lo], num[i] = num[i], num[lo]
                self.p_wrapper(num, lo+1, hi, rst)
                num[lo], num[i] = num[i], num[lo]


if __name__ == '__main__':
    s = Solution()
    print s.permuteUnique(map(int, sys.argv[1].split(',')))
