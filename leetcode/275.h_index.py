#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from oj_helper import *

class Solution:
    def hIndex(self, citations):
        print citations
        return self.h_wrapper(citations, 0, len(citations)-1, 0)

    def h_wrapper(self, citations, sidx, eidx, h_offset):
        if sidx > eidx:
            return h_offset
        elif sidx == eidx:
            return h_offset + (1 if citations[sidx] >= (h_offset + 1) else 0)

        cit_len = eidx -  sidx + 1
        if (eidx - sidx) < 100:
            hidx = h_offset
            for i in range(cit_len-1, -1, -1):
                if (h_offset + cit_len - i) <= citations[i]:
                    hidx = max(hidx, h_offset + cit_len - i)
            return hidx

        mid = (eidx + sidx + 1) // 2
        if citations[mid] >= (h_offset + eidx - mid + 1):
            # on the left
            return self.h_wrapper(citations, sidx,
                                  mid - 1, h_offset + eidx - mid + 1)
        return self.h_wrapper(citations, mid, eidx, h_offset)

if __name__ == '__main__':
    s = Solution()
    cats = [3, 0, 6, 1, 5]
    cats.sort()
    print s.hIndex(cats)
    print s.hIndex([4] * 10)
    print s.hIndex([1, 2, 2, 2])
    print s.hIndex([1, 1, 2, 2])
    with open('275.data') as f:
        cits = map(int,
                   f.readline().split(','))
        print s.hIndex(cits)
