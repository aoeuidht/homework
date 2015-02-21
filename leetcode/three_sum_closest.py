#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""

class Solution:
    def find_biggest_not_large(self, num, lo, hi, tgt):
        if lo > hi:
            # this only happen when mv > tgt
            # so we only return lo - 1
            return lo - 1
        if (lo == hi):
            if num[lo] > tgt:
                return lo - 1
            else:
                return lo

        mid = (lo + hi) / 2
        mv = num[mid]
        if mv > tgt:
            return self.find_biggest_not_large(num, lo, mid-1, tgt)
        else:
            return self.find_biggest_not_large(num, mid+1, hi, tgt)

    def abs(self, n):
        return n if n >=0 else -n

    def ts_wrapper(self, num, tgt):
        num.sort()
        r_n = num[0]+num[1]+num[2]
        r_v = self.abs(r_n - tgt)
        nl = len(num)
        for i in xrange(nl-2):
            n_i = num[i]
            for j in xrange(i+1, nl-1):
                n_j = num[j]
                _t = tgt - (n_i + n_j)
                piv = self.find_biggest_not_large(num, j+1, nl-1, _t)
                _l = _h = r_v + 1

                # check piv and piv+1 only, if piv+2 < len(num)
                if piv > j:
                    _l_v = n_i + n_j + num[piv]
                    _l = self.abs(_l_v - tgt)
                    if _l < r_v:
                        r_v = _l
                        r_n = _l_v
                if (piv+2) <= nl:
                    _h_v = n_i + n_j + num[piv+1]
                    _h = self.abs(_h_v - tgt)
                    if _h < r_v:
                        r_v = _h
                        r_n = _h_v
                if r_v == 0:
                    return r_n
        return r_n


    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSumClosest(self, num, target):
        nl = len(num)
        if nl < 4:
            return sum[num]
        return self.ts_wrapper(num, target)

if __name__ == '__main__':
    s = Solution()
    print s.threeSumClosest(map(int, sys.argv[1].split(',')), int(sys.argv[2]))
