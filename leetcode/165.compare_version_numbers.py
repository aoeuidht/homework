#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        l1, l2 = len(v1), len(v2)

        for i in range(min(l1, l2)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1

        if l1 > l2:
            return 1 if any(v1[l2:]) else 0
        elif l1 < l2:
            return -1 if any(v2[l1:]) else 0
        return 0

if __name__ == '__main__':
    s = Solution()
    r = s.compareVersion(sys.argv[1], sys.argv[2])
    print r
