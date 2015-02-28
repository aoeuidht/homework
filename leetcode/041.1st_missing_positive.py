#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        al = len(A)

        for i in range(al):
            if (A[i] == i+1) or (A[i] <= 0):
                continue
            while True:
                idx = A[i] - 1
                # out of range, or a infinite loop
                if (idx > (al -1)) or (idx < 0) or (A[i] == A[idx]):
                    A[i] = -1
                    break
                A[i], A[idx] = A[idx], A[i]
                if (A[i] == i+1) or (A[i] < 0):
                    break
        print A
        i = 0
        while i < al:
            if A[i] != (i+1):
                break
            i += 1


        return i + 1

if __name__ == '__main__':
    s = Solution()
    print s.firstMissingPositive(map(int, sys.argv[1].split(',')) if sys.argv[1] else [])
