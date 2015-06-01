#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        l1 = len(nums)
        if l1 <= k:
            l2 = len(set(nums))
            return not (l1 == l2)

        if k < 1:
            return False

        s = set(nums[:k])
        for i in range(k, l1):
            s.add(nums[i])
            if len(s) < k+1:
                return True
            o_val = nums[i-k]
            print o_val
            s.remove(o_val)
        return False


if __name__ == '__main__':
    s = Solution()
    print s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
    print s.containsNearbyDuplicate([4, 1, 2, 3, 1, 5], 3)
