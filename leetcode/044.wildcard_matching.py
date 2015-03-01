#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        # merge dup * in p
        if p:
            prev = ord(p[0])
            _p = [p[0]]
            for i in range(1, len(p)):
                if prev == 42:
                    if ord(p[i]) == 42:
                        continue
                _p.append(p[i])
                prev = ord(p[i])
            p = ''.join(_p)
        return self.m_wrapper(s, 0, len(s)-1, p, 0, len(p)-1)

    def find_star(self, p, lo, hi):
        # find * position from left to right
        # and from right to left
        if lo > hi:
            return -1, -1
        l, h = -1, -1
        for i in range(lo, hi+1):
            if ord(p[i]) == 42:
                l = l if l > -1  else i
                h = i
        return l, h

    def m_wrapper(self, s, s_lo, s_hi, p, p_lo, p_hi):
        # *: 42, ?: 63
        so = s_lo > s_hi
        po = p_lo > p_hi
        if not (so is po):
            if so:
                return True if p[p_lo:p_hi+1] == '*' * (p_hi+1-p_lo) else False
            return False
        elif so:
            return True

        star_lo, star_hi = self.find_star(p, p_lo, p_hi)
        # check left
        if star_lo > p_lo:
            slen = star_lo - p_lo
            if s[s_lo:s_lo+slen] != p[p_lo: star_lo]:
                pass
                return False
        # check right
        if -1 < star_hi < p_hi:
            slen = p_hi - star_hi
            slo = s_hi - slen + 1
            if (slo < s_lo) or (s[slo:s_hi+1] != p[star_hi+1: p_hi+1]):
                return False

        pc = ord(p[p_lo])
        sc = ord(s[s_lo])
        if (p_lo == p_hi) and (pc == 42):
            return True
        if pc == 42:
            return (self.m_wrapper(s, s_lo+1, s_hi, p, p_lo+1, p_hi) or
                    self.m_wrapper(s, s_lo+1, s_hi, p, p_lo, p_hi) or
                    self.m_wrapper(s, s_lo, s_hi, p, p_lo+1, p_hi))
        elif (pc == 63) or (pc == sc):
            return self.m_wrapper(s, s_lo+1, s_hi, p, p_lo+1, p_hi)
        return False

if __name__ == '__main__':
    s = Solution()
    print s.isMatch(*sys.argv[1:])
