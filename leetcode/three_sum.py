#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""

class Solution:
    def find_tgt(self, num, lo, hi, tgt):
        print lo, hi, tgt
        if lo > hi:
            return -1
        if (lo == hi):
            if num[lo] == tgt:
                return tgt
            else:
                return -1
        mid = (lo + hi) / 2
        mv = num[mid]
        if mv > tgt:
            return self.find_tgt(num, lo, mid-1, tgt)
        elif mv == tgt:
            return tgt
        else:
            return self.find_tgt(num, mid+1, hi, tgt)

    def ts_wrapper(self, num):
        nd = {}
        for n in num:
            _l = nd.get(n, 0)
            _l += 1
            nd[n] = _l

        num.sort()
        rst_cache = {}
        nl = len(num)
        for i in xrange(nl-2):
            n_i = num[i]
            if n_i >= 0:
                break
            for j in xrange(i+1, nl-1):
                n_j = num[j]
                if (n_i + n_j) >= 0:
                    break
                t = -(n_i + n_j)
                if (t >= n_j) and nd.has_key(t):
                    if (t == n_j) and (nd[t] < 2):
                        continue
                    ck = '%d_%d' % (n_i, n_j)
                    if not rst_cache.has_key(ck):
                        yield [n_i, n_j, t]
                        rst_cache[ck] = 1
        if nd.get(0, 0) > 2:
            yield [0, 0, 0]

    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        rst = []
        for r in self.ts_wrapper(num):
            rst.append(r)
        return rst

if __name__ == '__main__':
    s = Solution()
    print s.threeSum(map(int,
                         sys.argv[1].split(',')))
