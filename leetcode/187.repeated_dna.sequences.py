#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from oj_helper import *

class Solution:
    # @param s, a string
    # @return a string[]
    def findRepeatedDnaSequences(self, s):
        sl = len(s)
        char_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        dna_set = set()
        val = 0
        vmask = (1 << 20) - 1
        for i in range(10):
            val = (val << 2) + char_map[s[i]]
        dna_set.add(val)
        #print "{0:20b}".format(vmask)
        #print "{0:20b}".format(val), val
        int_set = set()
        for i in range(10, sl):
            val = (val << 2) + char_map[s[i]]
            val &= vmask
            #print "{0:20b}".format(val), val
            if val in dna_set:
                int_set.add(val)
            else:
                dna_set.add(val)

        return map(self.int2str, int_set)

    def int2str(self, i):
        int_map = ['A', 'C', 'G', 'T']
        r = []
        for c in range(10):
            r.append(int_map[i % 4])
            i = i >> 2
        return ''.join(r[::-1])

if __name__ == '__main__':
    s = Solution()
    r = s.findRepeatedDnaSequences(sys.argv[1])
    print r
