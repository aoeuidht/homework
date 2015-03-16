#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        #r, w, b, cur
        mk = [-1] * 3
        for cur, v in enumerate(A):
            if v == 2:
                if mk[v] < 0:
                    mk[v] = cur
            else:
                # move the right ones
                start, end = -1, cur
                for i in range(2, v, -1):
                    start = mk[i]
                    if start < 0:
                        continue
                    A[end] = i
                    mk[i] += 1
                    A[start] = v
                    end = start
                if start < 0:
                    mk[v] = cur if mk[v] < 0 else mk[v]
                else:
                    if mk[v] < 0:
                        mk[v] = start
            print cur, A[:cur+1]
        print A

if __name__ == '__main__':
    s = Solution()
    print s.sortColors(map(int, sys.argv[1:]))
