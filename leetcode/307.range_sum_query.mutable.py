#!/usr/bin/env python
# -*- coding: utf-8 -*-

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nl = len(nums)
        self.nums = nums

        self.block = 64
        self.bsums = []
        for i in range(0, self.nl, self.block):
            self.bsums.append(sum(self.nums[i: i+ self.block]))

    def update(self, i, val):
        if i >= self.nl:
            return
        self.nums[i] = val
        bidx = i / self.block
        self.bsums[bidx] = None

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if j >= self.nl:
            return 0

        # split i, j to tails and blocks
        rst = 0
        j += 1
        while i < j:
            if (((i % self.block) == 0) and
                ((j - i) >= self.block)):
                    bidx = i / self.block
                    if self.bsums[bidx] is None:
                        self.bsums[bidx] = sum(self.nums[i: i + self.block])
                    rst += self.bsums[i / self.block]
                    i += self.block
            else:
                rst += self.nums[i]
                i += 1
        return rst


# Your NumArray object will be instantiated and called as such:
nums = range(1, 256)
numArray = NumArray(nums)
import sys
x, y, i, v = map(int, sys.argv[1:])
print len(nums)
print numArray.sumRange(x, y), sum(nums[x: y+1])
numArray.update(i, v)
print numArray.sumRange(x, y), sum(nums[x: y+1])
