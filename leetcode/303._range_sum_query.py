#!/usr/bin/env python
# -*- coding: utf-8 -*-

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nl = len(nums)
        self.nums = [0] * (self.nl + 1)
        for i in range(self.nl):
                self.nums[i+1] = self.nums[i] + nums[i]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if j >= self.nl:
            return 0
        return self.nums[j + 1] - self.nums[i]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)
print numArray.sumRange(0, 2)
print numArray.sumRange(2, 5)
print numArray.sumRange(0, 5)
