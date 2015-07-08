#!/usr/bin/env python

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        rst = []
        nl = len(nums)
        if nl == 0:
            return rst
        elif nl == 1:
            rst.append(str(nums[0]))
            return rst
        prev = nums[0]
        rstr = ''
        for idx in range(1, nl):
            cur = nums[idx]
            if cur == (prev + 1):
                if not rstr:
                    rstr = '%d->' % prev
            else:
                rst.append('%s%d' % (rstr, prev))
                rstr = ''
            prev = cur
        rst.append('%s%d' % (rstr, prev))
        return rst

if __name__ == '__main__':
    s = Solution()
    print s.summaryRanges([0,1,2,4,5,7])
    print s.summaryRanges(range(3, 10, 3))
    print s.summaryRanges(range(3, 10))
