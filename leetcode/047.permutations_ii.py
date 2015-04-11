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
        s = set([l])

        for i in range(lo, hi+1):
            if (l == num[i]):
                if i == lo:
                    self.p_wrapper(num, lo+1, hi, rst)
            else:
                if num[i] in s:
                    continue
                s.add(num[i])
                num[lo], num[i] = num[i], num[lo]
                self.p_wrapper(num, lo+1, hi, rst)
                num[lo], num[i] = num[i], num[lo]


if __name__ == '__main__':
    s = Solution()
    # -1,2,0,-1,1,0,1
    r = s.permuteUnique(map(int, sys.argv[1].split(',')))
    print len(r), len(set(map(lambda x: '_'.join(map(str, x)),
                              r)))
