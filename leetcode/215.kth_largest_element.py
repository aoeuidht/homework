#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    def findKthLargest(self, nums, k):
        print 'calc', nums, k
        nl = len(nums)
        if k == 1:
            return max(nums)
        elif k == nl:
            return min(nums)
        if nl < 1000:
            nums.sort()
            return nums[-k]
        # use nums[0] as pivort
        nums[0], nums[1] = max(nums[0], nums[1]), min(nums[0], nums[1])
        cur = 1
        piv = nums[0]
        for i in range(2, nl):
            if nums[i] >= piv:
                nums[cur], nums[i] = nums[i], nums[cur]
                cur += 1
        cnt_bg_piv = cur
        if cur < k:
            return self.findKthLargest(nums[cur:], k - cur)
        else:
            return self.findKthLargest(nums[:cur], k)

if __name__ == '__main__':
    s = Solution()
    print s.findKthLargest(map(int, sys.argv[1].split(',')),
                           int(sys.argv[2]))
