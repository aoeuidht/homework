#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    def reverse_array(self, num, lo, hi):
        while lo < hi:
            num[lo], num[hi] = num[hi], num[lo]
            lo += 1
            hi -= 1

    def insertion_sort(self, num, lo, hi):
        for i in range(lo+1, hi+1):
            for j in range(i, lo, -1):
                if num[j] < num[j-1]:
                    num[j-1], num[j] = num[j], num[j-1]
                else:
                    break

    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        nl = len(num)
        if nl < 2:
            return num

        loc = -1
        for j in range(nl-1, 0, -1):
            if num[j] > num[j-1]:
                loc = j - 1
                break

        #now we have an array like " 4 5 3 2 1 "
        if loc > -1:
            # sort the array num[j-1:]
            loc_val = num[loc]
            # we have to find the minium one bigger than the num[loc]
            # so we swap it first
            num[loc], num[loc+1] = num[loc+1], num[loc]
            for i in range(loc+1, nl):
                # find the minium in bigger
                if (num[i] > loc_val) and (num[loc] > num[i]):
                    num[loc], num[i] = num[i], num[loc]
            self.reverse_array(num, loc+1, nl-1)
            self.insertion_sort(num, loc+1, nl-1)
        else:
            # if the array is in reverse order,
            # just reverse it again
            self.reverse_array(num, 0, nl-1)
        return num

if __name__ == '__main__':
    s = Solution()
    print s.nextPermutation(map(int, sys.argv[1].split(',')))
