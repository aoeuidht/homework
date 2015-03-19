#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    def __init__(self):
        pass

    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        al = len(A)
        if al == 0:
            return 0
        if al == A[-1]:
            return al

        cur = 0
        i = 1
        dc = 0
        while i < al:
            _d = True if (A[cur] == A[i]) else False
            i += 1
            if (_d and (dc > 0)):
                continue
            dc = 1 if _d else 0
            cur += 1
            A[cur] = A[i-1]
        A[cur+1:] = []
        return cur+1

if __name__ == '__main__':
    s = Solution()
    p = map(int, sys.argv[1:])
    r = s.removeDuplicates(p)
    print r, p
