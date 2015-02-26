#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        slen = len(s)
        m_map = [-1] * slen
        buf = []
        cur = 0
        rst = 0
        lo, hi = -1, -1
        for _idx, _c in enumerate(list(s)):
            c = ord(_c)
            if c == 40:
                buf.append((_idx, c))
            else:
                if (not buf) or (buf[-1][1] != 40):
                    buf[:] = []
                    cur = 0
                    continue
                idx, _ = buf.pop()
                m_map[_idx], m_map[idx] = idx, _idx
                while (idx > 1) and (m_map[idx-1] > -1):
                    idx = m_map[idx-1]
                cur = _idx - idx + 1
                if cur > rst:
                    lo = idx
                    hi = _idx
                    rst = cur
        return rst

if __name__ == '__main__':
    s = Solution()
    print s.longestValidParentheses(sys.argv[1])
