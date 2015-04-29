#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        n -= 1
        if n < 2:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 2

        #marks = [0] * ((n + 32) / 32)
        #marks = bitarray(n+1)
        marks = [0] * (n + 1)
        x = 2
        while True:
            if (x ** 2) > n:
                break
            #if self.is_prime(marks, x):
            if marks[x] == 0:
                j = x * 2
                while j <= n:
                    marks[j] = 1
                    j += x
            x += 1

        # count all the zeros
        r = 2
        for x in xrange(5, n+1):
            r += 1 if (marks[x] == 0) else 0
        return r

    def set_not_prime(self, marks, idx):
        marks[idx] = 1
        return
        _i = idx / 32
        v = marks[_i]
        offset = idx % 32
        mask = 1 << offset
        marks[_i] = v | mask
        return

    def is_prime(self, marks, idx):
        return marks[idx] == 0
        v = marks[idx / 32]
        offset = idx % 32
        mask = 1 << offset
        return (v & mask) == 0

if __name__ == '__main__':
    s = Solution()
    print s.countPrimes(int(sys.argv[1]))
