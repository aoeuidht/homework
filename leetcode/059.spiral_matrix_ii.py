#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0:
            return []
        return self.gen_part(1, n, [], [])

    def gen_part(self, lo, n, prefix, suffix):
        if n == 1:
            return [((prefix[0] + [lo] + suffix[0])
                     if prefix
                     else [lo])]
        # top
        top = ((prefix[0] + range(lo, lo+n) + suffix[0])
               if prefix
               else range(lo, lo+n))

        # mid
        n_prefix = []
        n_suffix = []
        for i in range(1, n-1):
            _p = prefix[i] if prefix else []
            _p.append(lo+4*n-4-i)
            n_prefix.append(_p)
            _s = [lo+n-1+i] + (suffix[i] if prefix else [])
            n_suffix.append(_s)

        mid = []
        if n > 2:
            mid = self.gen_part(lo+4*n-4, n-2, n_prefix, n_suffix)
        #bottom
        bottom = ((prefix[n-1] + range(lo+3*n-3, lo+2*n-3, -1) + suffix[n-1])
                  if prefix
                  else range(lo+3*n-3, lo+2*n-3, -1))
        return [top] + mid + [bottom]

if __name__ == '__main__':
    s = Solution()
    r = s.generateMatrix(int(sys.argv[1]))
    for i in r:
        print '\t'.join(map(str, i))
