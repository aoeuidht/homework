#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oj_helper import *

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        nl = len(nums)
        if not nums:
            return []

        if k < 2:
            return nums

        if nl <= k:
            return [max(nums)]

        rst = [0] * (nl - k + 1)

        m_idx = 0
        m = nums[0]
        # init the k-1 items
        for i in range(1, k-1):
            if m < nums[i]:
                m = nums[i]
                m_idx = i

        pl, lr = 0, k-1
        while lr < nl:
            # check weather we have to move the pivort
            if m_idx < pl:
                # re calculate the piv
                m_idx = pl
                m = nums[pl]
                for i in range(pl, lr+1):
                    if m < nums[i]:
                        m = nums[i]
                        m_idx = i

            # count the maximun
            if m < nums[lr]:
                m = nums[lr]
                m_idx = lr
            rst[lr-k+1] = m
            pl += 1
            lr += 1
        return rst

if __name__ == '__main__':
    s = Solution()
    print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 10)
