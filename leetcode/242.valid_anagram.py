#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from oj_helper import *

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        sd, td = {}, {}
        for i in range(len(s)):
            c = s[i]
            sd[c] = sd.get(c, 0) + 1
            c = t[i]
            td[c] = td.get(c, 0) + 1

        for c, n in sd.iteritems():
            if n != td.get(c, 0):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.isAnagram('anagram', 'nagaram')
    print s.isAnagram('cat', 'rat')
