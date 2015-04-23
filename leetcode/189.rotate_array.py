#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        if not nums:
            return nums
        nl = len(nums)
        k %= nl
        if (k == 0):
            return
        k = nl - k
        tmp = nums[:k]
        nums[:nl-k] = nums[k:]
        nums[nl-k:] = tmp
        print nums

if __name__ == '__main__':
    s = Solution()
    s.rotate(map(int, sys.argv[1].split(',')),
             int(sys.argv[2]))
