#!/usr/bin/env python

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0

        start = 0
        total = nums[0]
        if total >= s:
            return 1
        nl = len(nums)
        rst = nl + 1

        for piv in range(1, nl):
            total += nums[piv]
            print 'outer', total, nums[start: piv+1], rst
            if total < s:
                continue
            else:
                rst = min(piv - start + 1,
                          rst)
            for start in range(start, piv+1):
                total -= nums[start]
                if total < s:
                    start += 1
                    break
                rst = min(piv - start ,
                          rst)
        return 0 if rst > nl else rst


if __name__ == '__main__':
    s = Solution()
    print s.minSubArrayLen(7, [2,3,1,2,4,3])
    print s.minSubArrayLen(40, [2,3,1,2,4,3])
    print s.minSubArrayLen(5, [2,3,1,1,1,1,1])
