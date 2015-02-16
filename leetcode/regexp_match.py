#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
"""

import sys

class Solution:
    def __init__(self):
        self.rst_tmp = {}

    def reg_to_tk(self, p):
        if p[0] == '*':
            return []

        pl = len(p)
        i = 0
        rst = []
        while i < pl:
            c = p[i]
            if c == '*':
                rst[-1] = '%s*' % rst[-1]
            else:
                rst.append(c)
            i += 1
        return rst

    def tk_match(self, c, tk):
        """return (matched, step)"""
        m, step = False, 1
        # match c or .
        if (ord(c) == ord(tk[0])) or (ord(tk[0]) == 46):
            m = True
        # check *
        if ord(tk[-1]) == 42:
            step = 0
        return m, step

    #def chk_

    def match_wrapper(self, s, sl, ptk, pl):
        k = '%d_%d' % (sl, pl)
        if self.rst_tmp.has_key(k):
            return self.rst_tmp[k]
        slen = len(s)
        plen = len(ptk)
        rst = False

        if (sl > (slen-1)) or (pl > (plen-1)):
            if (sl > (slen-1)) and (pl > (plen-1)):
                rst = True
            elif sl > (slen-1):
                # if all the left token are *, then return True
                if all([(ord(t[-1]) == 42) for t in ptk[pl:]]):
                    rst = True
                else:
                    rst = False
            else:
                rst = False
        else:
            m, step = self.tk_match(s[sl], ptk[pl])
            if step > 0:
                if not m:
                    rst = False
                else:
                    rst = self.match_wrapper(s, sl+1, ptk, pl+1)
            else:
                # when a * match, 3 cases

                if m:
                    rst = (self.match_wrapper(s, sl+1, ptk, pl) or
                           self.match_wrapper(s, sl+1, ptk, pl+1) or
                           self.match_wrapper(s, sl, ptk, pl+1))
                else:
                # when * not match, 1 case
                    rst = self.match_wrapper(s, sl, ptk, pl+1)
        self.rst_tmp[k] = rst
        return rst

    # @return a boolean
    def isMatch(self, s, p):
        if not p:
            return False if s else True
        ptk = self.reg_to_tk(p)
        return self.match_wrapper(s, 0, ptk, 0)

if __name__ == '__main__':
    s = Solution()
    print s.isMatch(sys.argv[1], sys.argv[2])
