#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        cmap, cmaped = {}, {}

        for i in range(len(s)):
            cs, ct = s[i], t[i]
            # checket cmap
            if cmap.has_key(cs):
                if ord(cmap[cs]) != ord(ct):
                    return False
            else:
                # check weather ct has been mapped
                if cmaped.has_key(ct):
                    return False
                cmap[cs] = ct
                cmaped[ct] = cs
        return True

if __name__ == '__main__':
    s = Solution()
    print s.isIsomorphic(*sys.argv[1:])
