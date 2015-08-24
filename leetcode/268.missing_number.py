#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oj_helper import *

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        r = 0
        _xor = 0
        for n in nums:
            _xor ^= r
            _xor ^= n
            r += 1
        _xor ^= r
        return _xor
