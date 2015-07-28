#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oj_helper import *

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        nl = len(nums)
        if not nl:
            return []
        rst = [1] * nl

        for i in range(1, nl):
            rst[i] = rst[i-1] * nums[i-1]

        # product it back
        p = nums[nl-1]
        for i in range(nl-2, -1, -1):
            rst[i] *= p
            p *= nums[i]

        return rst

if __name__ == '__main__':
    s = Solution()
    print s.productExceptSelf([1,2,3, 4])
    print s.productExceptSelf([1,2, 3])
    print s.productExceptSelf([1,2])
    print s.productExceptSelf([1])
    print s.productExceptSelf([])
