#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from oj_helper import *

class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return self.h_wrapper(citations, 0, len(citations)-1, 0)

    def h_wrapper(self, citations, sidx, eidx, h_offset):
        #print citations[sidx], sidx, eidx, h_offset
        if sidx > eidx:
            return h_offset
        elif sidx == eidx:
            return h_offset + (1 if citations[sidx] >= (h_offset + 1) else 0)

        cit_len = eidx - sidx + 1
        if (eidx - sidx) < 1000:
            #print 'go-stort'
            tmp_cit = citations[sidx: eidx+1]
            tmp_cit.sort()
            #print tmp_cit
            hidx = h_offset
            for i in range(cit_len-1, -1, -1):
                if (h_offset + cit_len - i) <= tmp_cit[i]:
                    hidx = max(hidx, h_offset + cit_len - i)
            return hidx

        # use the 1st as the pivort
        piv = citations[sidx]
        spt = sidx
        for i in range(sidx+1, eidx + 1):
            if citations[i] > piv:
                spt += 1
                if spt < i:
                    citations[spt], citations[i] = citations[i], citations[spt]

        # ceit[sidx: spt+1] are smaller than piv
        citations[spt], citations[sidx] = citations[sidx], citations[spt]
        cnum = spt - sidx + 1
        if h_offset + cnum <= piv:
            # on the right
            return self.h_wrapper(citations, spt+1, eidx, h_offset + cnum)
        else:
            # on the left
            return self.h_wrapper(citations, sidx, spt, h_offset)


if __name__ == '__main__':
    s = Solution()
    print s.hIndex([3, 0, 6, 1, 5])
    print s.hIndex([4] * 10)
    print s.hIndex([1, 2, 2, 2])
    with open('274.data') as f:
        cits = map(int,
                   f.readline().split(','))
        print s.hIndex(cits)
        cits.sort()
        cits = cits[::-1]
        print len(cits), cits[0]
        print cits[1030], cits[1031], cits[9999]
