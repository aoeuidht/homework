#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        l1 = len(nums)
        if l1 < 2:
            return False
        if k < 1:
            return False
        s = set([nums[0]])
        vmax, vmin = nums[0], nums[0]
        for idx in range(1, l1):
            v = nums[idx]
            if t > k:
                head, tail = v-t, v+t
                for i in s:
                    if head <= i <= tail:
                        return True
            else:
                for i in range(v-t, v+t+1):
                    if i in s:
                        return True
            s.add(v)
            if idx >= k:
                s.remove(nums[idx-k])
        return False


if __name__ == '__main__':
    s = Solution()
    print s.containsNearbyAlmostDuplicate([1, 3, 1], 2, 1)
    print s.containsNearbyAlmostDuplicate([7, 1, 3], 2, 3)
