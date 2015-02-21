#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

""""""

class Solution:
    def digit_to_list(self, digit):
        dmap = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}
        return dmap[digit]

    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if not digits:
            return ['']
        if len(digits) == 1:
            return self.digit_to_list(digits)
        return reduce(lambda s1, s2: ['%s%s' % (i, j) for i in s1 for j in s2],
                      map(self.digit_to_list, list(digits)))

if __name__ == '__main__':
    s = Solution()
    print s.letterCombinations(sys.argv[1])
