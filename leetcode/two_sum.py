#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        n_c = len(num)
        d = {}
        for i, j in enumerate(num):
            d.setdefault(j, [])
            d[j].append(i+1)
        num.sort()
        n_c = len(num)
        i, j = 0, n_c -1
        while True:
            if num[i] + num[j] == target:
                l = r = 0
                if num[i] == num[j]:
                    l, r = (d[num[i]][0], d[num[i]][1])
                else:
                    l, r = (d[num[i]][0], d[num[j]][0])
                return (l, r) if (r > l) else (r, l)
            if (num[i] + num[j]) > target:
                j -= 1
            else:
                i += 1
            if i >= j:
                return (-1, -1)


if __name__ == '__main__':
    s = Solution()
    print s.twoSum([0, 4, 3, 0], 0)
