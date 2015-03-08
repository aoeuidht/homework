#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @return a string
    def getPermutation(self, n, k):

        raw = range(1, n+1)
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = i * factorial[i-1]

        offset = k - 1
        lo = 0
        raw_len = n
        while True:
            if offset < 1:
                break
            step = factorial[n-1]
            swap_idx = offset / step
            if swap_idx > 0:
                if (lo + swap_idx) >= raw_len:
                    return ''
                # do the swap and sort operation
                raw[lo], raw[lo+swap_idx] = raw[lo+swap_idx], raw[lo]
                for _i in range(lo+swap_idx, lo+1, -1):
                    raw[_i], raw[_i-1] = raw[_i-1], raw[_i]
            n -= 1
            offset %= step
            lo += 1
        return raw
        return ''.join(map(str, raw))

if __name__ == '__main__':
    s = Solution()
    for i in range(1, int(sys.argv[2])+1):
        print i, s.getPermutation(int(sys.argv[1]), i)
