#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        buf = [i for i in s.split(' ') if i]
        return ' '.join(buf[::-1])

if __name__ == '__main__':
    s = Solution()
    r = s.reverseWords(sys.argv[1])
    print r, len(r)
