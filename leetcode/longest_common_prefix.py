#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution:
    def lcp_wrapper(self, strs, offset):
        if len(strs[0]) <= offset:
            return offset
        c = ord(strs[0][offset])
        for s in strs:
            if (len(s) <= offset) or (ord(s[offset]) != c):
                return offset
        return self.lcp_wrapper(strs, offset+1)

    # @return a string
    def longestCommonPrefix(self, strs):
        #strs.sort()
        if not strs:
            return ''
        sl = len(strs)
        if sl < 2:
            return strs[0]
        l = self.lcp_wrapper(strs, 0)
        return strs[0][:l]

if __name__ == '__main__':
    s = Solution()
    print s.longestCommonPrefix(sys.argv[1:])
