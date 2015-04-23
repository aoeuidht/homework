#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param num, an integer[]
    # @return a string
    def largestNumber(self, num):
        if not any(num):
            return '0'

        ns = map(str, num)

        def l_cmp(s1, s2):
            o1, o2 = s1, s2
            l1, l2 = len(s1), len(s2)
            if l2 > l1:
                s1 = '%s%s' % (s1, s1[0] * (l2 - l1))
            elif l1 > l2:
                s2 = '%s%s' % (s2, s2[0] * (l1 - l2))

            if s1 > s2:
                rst = -1
            elif s1 < s2:
                rst = 1
            else:
                rst = 0
                if l1 <> l2:
                    c1 = s1[0]
                    for i in range(1, l1):
                        c2 = s1[i]
                        if c1 == c2:
                            continue
                        if c1 > c2:
                            rst = 1 if (l1 < l2) else -1
                        else:
                            rst = -1 if (l1 < l2) else 1
                        break
            print o1, o2, rst
            return rst
        print sorted(ns, cmp=l_cmp)
        return ''.join(sorted(ns, cmp=l_cmp))

if __name__ == '__main__':
    s = Solution()
    r = s.largestNumber(map(int, sys.argv[1].split(',')))
    print r
