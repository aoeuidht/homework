#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        if not height:
            return 0

        rst = 0
        stack = []
        height.append(0)
        for i, v in enumerate(height):
            if (not stack) or (height[stack[-1]] <= v):
                stack.append(i)
                continue
            #
            while True:
                if stack and (height[stack[-1]] >= v):
                    _i = stack.pop()
                    _h = height[_i]
                    rst = max(rst,
                              _h * ((i - stack[-1] - 1) if stack
                                    else i))
                else:
                    break
            stack.append(i)
        while stack:
            _i = stack.pop()
            _h = height[_i]
            rst = max(rst,
                      _h * ((i - _i) if stack else i))

        return rst

if __name__ == '__main__':
    s = Solution()
    print s.largestRectangleArea([2,1,5,6,2,3])
