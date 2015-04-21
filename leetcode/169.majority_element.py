#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        if len(num) < 3:
            return num[0]

        maj, cnt = None, 0
        for i in num:
            if cnt == 0:
                maj, cnt = i, 1
            else:
                if maj == i:
                    cnt += 1
                else:
                    cnt -= 1
        return maj

if __name__ == '__main__':
    s = Solution()
    r = s.majorityElement(int(sys.argv[1]))
    print r
