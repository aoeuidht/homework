#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        nl = len(numbers)
        left, right = 0, nl - 1
        if nl < 2:
            return []
        while left < right:
            vl, vr = numbers[left], numbers[right]
            sv = vl + vr
            if sv == target:
                return [left+1, right+1]
            elif sv > target:
                right -= 1
            else:
                left += 1
        return []

if __name__ == '__main__':
    s = Solution()
    print s.twoSum([0, 0, 3, 4], 0)
