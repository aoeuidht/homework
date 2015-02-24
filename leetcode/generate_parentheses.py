#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""

class Solution:
    def gen_wrapper(self, l, r, rst):
        lb, rb = [], []
        if r > l:
            # add the right one
            lb = self.gen_wrapper(l, r-1, ['%s%s' % (i, ')') for i in rst])
            if l > 0:
                rb = self.gen_wrapper(l-1, r, ['%s%s' % (i, '(') for i in rst])
            return lb + rb
        else:
            if l > 0:
                return self.gen_wrapper(l-1, r, ['%s%s' % (i, '(') for i in rst])
            return rst
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        return self.gen_wrapper(n-1, n, ['('])

if __name__ == '__main__':
    s = Solution()
    print s.generateParenthesis(int(sys.argv[1]))
