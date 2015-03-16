#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        row_idx = self.search_row(matrix, target, 0, len(matrix)-1)
        if row_idx < 0:
            return False
        return self.search_col(matrix[row_idx], target, 0, len(matrix[row_idx])-1)

    def search_row(self, matrix, target, lo, hi):
        if target < matrix[lo][0]:
            return lo-1
        elif target >= matrix[hi][0]:
            return hi

        if hi - lo < 5:
            for i in range(lo, hi):
                if matrix[i][0] <= target < matrix[i+1][0]:
                    return i
        # now split
        mid = (lo + hi) / 2
        if target >= matrix[mid][0]:
            return self.search_row(matrix, target, mid, hi)
        else:
            return self.search_row(matrix, target, lo, mid)

    def search_col(self, nums, target, lo, hi):
        if hi - lo < 5:
            for i in range(lo, hi+1):
                if nums[i] == target:
                    return True
            return False
        mid = (lo + hi) / 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            return self.search_col(nums, target, mid+1, hi)
        else:
            return self.search_col(nums, target, lo, mid-1)

if __name__ == '__main__':
    s = Solution()
    print s.searchMatrix([
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ], int(sys.argv[1]))
