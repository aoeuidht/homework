#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @return a string
    def countAndSay(self, n):
        prev = ['', '1', '11', '21', '1211']
        if n < 5:
            return prev[n]
        s = prev[4]
        for i in range(5, n+1):
            print i, s
            s = self.count_it(s)
        return s

    def count_it(self, s):
        if not s:
            return ''
        rst = [[1, s[0]]]
        for i in range(1, len(s)):
            c = s[i]
            if c == rst[-1][1]:
                rst[-1][0] += 1
            else:
                rst.append([1, c])
        return ''.join(map(lambda i: '%d%s' % (i[0], i[1]),
                           rst))

if __name__ == '__main__':
    s = Solution()
    print s.countAndSay(int(sys.argv[1]))
