#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""Implement atoi to convert a string to an integer."""

class Solution:
    def atoi_wrapper(self, s, lo, hi, r, limit):
        if lo > hi:
            return r

        ord0, ord9 = 48, 57
        so = ord(s[lo])
        if ord0 <= so <= ord9:
            rn = r * 10 + so - ord0
            if rn > limit:
                return limit
            return self.atoi_wrapper(s, lo+1, hi, rn, limit)
        return r

    # @return an integer
    def atoi(self, s):
        s = s.strip()
        slen = len(s) - 1
        if slen < 0:
            return 0
        c = s[0]
        # +
        oc = ord(c)
        if oc == 43:
            return self.atoi_wrapper(s, 1, slen, 0, 2147483647)
        # -
        elif oc == 45:
            return -self.atoi_wrapper(s, 1, slen, 0, 2147483648)
        return self.atoi_wrapper(s, 0, slen, 0, 2147483647)

if __name__ == '__main__':
    s = Solution()
    print s.atoi(sys.argv[1])
