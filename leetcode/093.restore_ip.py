#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        rst = []
        sl = len(s)
        for i in range(3, 0, -1):
            if (i >= sl):
                continue
            if (sl-i > 9):
                break
            _i = s[:i]
            if not self.chk_ip_section(_i):
                continue
            for j in range(3, 0, -1):
                if (i+j >= sl):
                    continue
                if sl-i-j > 6:
                    break
                _j = s[i:i+j]
                if not self.chk_ip_section(_j):
                    continue

                for k in range(3, 0, -1):
                    if (i+j+k >= sl):
                        continue
                    if (sl-i-j-k > 3):
                        break
                    _k = s[i+j:i+j+k]
                    if not self.chk_ip_section(_k):
                        continue

                    _p = s[i+j+k:]
                    if self.chk_ip_section(_p):
                        rst.append('%s.%s.%s.%s' % (_i, _j, _k, _p))

        return rst


    def chk_ip_section(self, sec):
        """

        Arguments:
        - `self`:
        - `sec`:
        """
        v = int(sec)
        if v == 0:
            return sec == '0'
        return (v < 256) and (sec[0] != '0')

if __name__ == '__main__':
    s = Solution()
    print s.restoreIpAddresses(sys.argv[1])
