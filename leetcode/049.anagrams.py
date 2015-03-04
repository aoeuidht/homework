#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        # split the strs by length
        d = {}
        for s in strs:
            s_list = list(s)
            s_list.sort()
            _s = ''.join(s_list)
            s_his = d.get(_s, [])
            s_his.append(s)
            d[_s] = s_his
        rst = []
        for _, a_list in d.iteritems():
            if len(a_list) > 1:
                rst += a_list
        return rst

if __name__ == '__main__':
    s = Solution()
    print s.anagrams(sys.argv[1:])
