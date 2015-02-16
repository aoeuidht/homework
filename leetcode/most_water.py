#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""
class Solution:
    # @return an integer
    def maxArea(self, height):
        left=0
        right=len(height)-1
        result=0
        while left<right:
            print result, height[left], height[right], right-left
            result=max(result,(right-left)*min(height[left],height[right]))
            if  height[left]<height[right]:
                left+=1
            else:
                right-=1

        return result

if __name__ == '__main__':
    s = Solution()
    with open('most_water.txt') as f:
        p = map(int, f.readline().split(','))
        f.close()
        print s.maxArea(p)
