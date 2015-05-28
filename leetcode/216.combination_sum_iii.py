#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        return [r[::-1] for r in  self.c_wrapper(k, n, 1)]

    # s: start with
    def c_wrapper(self, k, n, s):
        print k, n, s
        r = []
        if ((s > n / k) or
            (n / k > 9) or
            (s > 9)):
            print k, n, s, 'break'
            return []
        if (k == 1) and (s <= n):
            return [[n]]
        for d in range(s, (n / k) + 1):
            tr = self.c_wrapper(k-1,
                                n-d,
                                d+1)
            for _r in tr:
                _r.append(d)
                r.append(_r)
        print k, n, s, r
        return r




if __name__ == '__main__':
    s = Solution()
    print s.combinationSum3(* map(int, sys.argv[1:]))
