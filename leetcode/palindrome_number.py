#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""Determine whether an integer is a palindrome. Do this without extra space.
"""
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        i = 0
        _x = x
        while _x > 0:
            _x /= 10
            i += 1
        _x = i / 2
        i -= 1
        while _x > 0:
            if (x % 10) == (x / (10 ** i)):
                x = x % (10 ** i)
                x /= 10
                _x -= 1
                i -= 2
            else:
                break
        return True if _x < 1 else False

if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome(int(sys.argv[1]))
