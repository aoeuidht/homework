#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from oj_helper import *


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        nl = len(nums)
        idx, s, e = 0, 0, 0
        while idx < nl:
            if nums[idx] == 0:
                break
            idx += 1

        s = idx
        e = s
        while e < nl-1:
            e += 1
            if nums[e] == 0:
                continue
            nums[s], nums[e] = nums[e], nums[s]
            s += 1


if __name__ == '__main__':
    s = Solution()
    for i in ('0,1,0,3,12',
              '0,0,0,0,0',
              '0,0,0,0,1',
              '1,0,0,0,0',
              '1,0,0,0,1',
              '1,0,0,2,0',
    ):
        r = map(int, i.split(','))
        print r
        s.moveZeroes(r)
        print r
