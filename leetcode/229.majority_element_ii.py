#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        cache = [[0, 0], [0, 0], [0, 0]]
        for n in nums:
            # count it
            r = False
            for c in cache:
                if c[0] == n:
                    c[1] += 1
                    r = True
                    break
            if not r:
                for c in cache:
                    if c[1] == 0:
                        c[0] = n
                        c[1] = 1
                        break
            # erase the ones link games
            m = min(cache[0][1], cache[1][1], cache[2][1])
            if m:
                cache[0][1] -= m
                cache[1][1] -= m
                cache[2][1] -= m

        cands = [c[0] for c in cache if c[1] > 0]
        cc = [0] * 3

        # count the candidacies
        for n in nums:
            if n in cands:
                cc[cands.index(n)] += 1

        p = int(len(nums) / 3)
        return [i[0] for i in zip(cands, cc) if i[1] > p]


if __name__ == '__main__':
    s = Solution()
    print s.majorityElement([1, 2, 3, 4])
    print s.majorityElement([0, 0])
    print s.majorityElement([])
    print s.majorityElement([6,6,6,7,7])
