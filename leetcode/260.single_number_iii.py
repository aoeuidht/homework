#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oj_helper import *

class Solution:
    def singleNumber(self, nums):
        num_his = [0] * 32

        # step 1. calc the xor of two nums
        xor_of_2 = 0
        for n in nums:
            xor_of_2 ^= n

        # for any bit in the xor resurt, it should be in
        # either a or b, but not both/neither
        # x =      0b......100000
        # x & -x = 0b000000100000
        xor_of_2 &= -xor_of_2


        rst = [0, 0]
        for n in nums:
            idx = 1
            if n & xor_of_2:
                idx = 0
            rst[idx] ^= n
        return rst


if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([1, 2, 1, 3, 2, 5])
    print s.singleNumber([2,1,2,3,4,1])
