#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from oj_helper import *

class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        tks = []
        v = 0
        op_map = {'+': lambda x, y: x+y,
                  '-': lambda x, y: x-y,
                  '*': lambda x, y: x*y}
        for i in range(len(input)):
            c = input[i]
            if c in op_map:
                tks.append(v)
                tks.append(op_map[c])
                v = 0
            else:
                v = v * 10 + int(c)
        tks.append(v)
        rst = self.d_wrapper(tks, 0, len(tks)-1)
        rst.sort()
        return rst

    def d_wrapper(self, tokens, start, end):
        if start == end:
            return [tokens[start]]
        elif (start + 2) == end:
            return [tokens[start+1](tokens[start], tokens[end])]
        else:
            rst = []
            for i in range(start, end, 2):
                f = tokens[i+1]
                rstl = self.d_wrapper(tokens, start, i)
                rstr = self.d_wrapper(tokens, i+2, end)
                rst += [f(i, j)
                        for i in rstl
                        for j in rstr]
            return rst

if __name__ == '__main__':
    s = Solution()
    print s.diffWaysToCompute('2*3-4*5')
