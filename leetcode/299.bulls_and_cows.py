#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from oj_helper import *

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if (not secret) or (len(secret) != len(guess)):
            return '0A0B'

        # bulls count, cows count
        bc, cc = 0, 0
        secret_miss_count = {}
        guess_miss_count = {}
        for secret_char, guess_char in zip(secret, guess):
            if int(secret_char) == int(guess_char):
                bc += 1
                continue
            secret_miss_count[secret_char] = secret_miss_count.get(secret_char, 0) + 1
            guess_miss_count[guess_char] = guess_miss_count.get(guess_char, 0) + 1

        for k in guess_miss_count:
            cc += min(guess_miss_count[k],
                      secret_miss_count.get(k, 0))

        return '%dA%dB' % (bc, cc)


if __name__ == '__main__':
    s = Solution()
    print s.getHint('1807', '7810')
    print s.getHint('1123', '0111')
