#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        al = len(A)
        if al < 1:
            return 0
        elif al == 1:
            return A[0]
        max_product = A[0]
        neg_lo, neg_hi = None, None
        lo, hi = 0, None
        _p = 0
        for idx, a in enumerate(A):
            if a == 0:
                max_product = max(max_product, 0)
                hi = idx - 1
                if _p < 0:
                    max_product = self.calc_negative(A, lo, hi,
                                                     neg_lo, neg_hi,
                                                     _p, max_product)

                lo = idx + 1
                neg_lo, neg_hi = None, None
                _p = 0
                continue
            if a < 0:
                if neg_lo is None:
                    neg_lo = idx
                else:
                    neg_hi = idx
            _p = a if (_p == 0) else (_p * a)
            max_product = _p if (_p > max_product) else max_product
        hi = idx
        if _p < 0:
            max_product = self.calc_negative(A, lo, hi,
                                             neg_lo, neg_hi,
                                             _p, max_product)

        return max_product

    def calc_negative(self, A, lo, hi,
                      neg_lo, neg_hi,
                      p, max_product):
        if hi == lo:
            return max_product
        elif (hi - lo) == 1:
            return max(max_product, A[lo], A[hi])

        print lo, hi, neg_lo, neg_hi, p, max_product
        # try to remove the first part
        __p = p
        for i in range(neg_lo, -1, -1):
            if A[i] != 0:
                __p /= A[i]
            else:
                break
        max_product = __p if (__p > max_product) else max_product

        # try to remove the right part
        neg_hi = neg_hi if not (neg_hi is None) else neg_lo
        __p = p
        for i in range(neg_hi, len(A)):
            if A[i] != 0:
                __p /= A[i]
            else:
                break
        max_product = __p if (__p > max_product) else max_product
        return max_product

if __name__ == '__main__':
    s = Solution()
    r = s.maxProduct(map(int, sys.argv[1].split(',')))
    print r
