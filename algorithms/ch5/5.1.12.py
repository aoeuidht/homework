#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class Alphabet:
    def __init__(self, chars):
        self.chars = chars

    def toChar(self, index):
        return self.chars[index]

    def toIndex(self, char):
        return self.chars.find(char)

    def contains(self, char):
        return True if (self.chars.find(char) != -1) else False

    def R(self):
        return len(self.chars)

    def lgR(self):
        return math.ceil(math.log(self.R()) / math.log(2))

    def toIndices(s):
        rst = []
        for _s in s:
            rst.append(self.toIndex(_s))
        return rst

    def toChars(indices):
        rst = []
        for i in indices:
            rst.append(self.toChar(i))

        return ''.join(rst)




class LSD:

    @staticmethod
    def sort(a, a_s, w):
        """
        a: the list to sort
        a_s: alphaset
        w: sort on leading w characters
        """
        R = a_items[0].R()
        N = len(a_items)

        aux = [None] * N

        for d in range(w-1, -1, -1):
            count = [0] * (R+1)

            for i in range(N):
                count[a_s.toIndex(a[i][d]) + 1] += 1

            for r in range(R):
                count[r+1] += count[r]

            for i in range(N):
                aux[count[a_s.toIndex(a[i][d])]+1] = a[i]
                count[a_s.toIndex(a[i][d])] += 1

            a[:] = aux[:]
