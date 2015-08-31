#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from oj_helper import *

class Solution:
    def __init__(self):
        """

        Arguments:
        - `self`:
        """
        self.e10 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five',
                      'Six', 'Seven', 'Eight', 'Nine', 'Ten']
        self.e20 = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
                       'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty']
        self.e100 = ['Zero', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty',
                        'Sixty', 'Seventy', 'Eighty', 'Ninety']
        self.others = {100: 'Hundred',
                       1000: 'Thousand'}

        self.k3 = ['', 'Thousand', 'Million', 'Billion', 'Trillion']

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1:
            return 'Zero'

        n = num
        segs = []
        while n:
            segs.append(self._to_word(n % 1000))
            n /= 1000

        words = []
        met_zero = False
        _no = -1
        for idx, seg in enumerate(segs):
            _n, word = seg
            if _n:
                sep = self.k3[idx]
                word.append(sep)
                w = ' '.join(word).strip()

                # add the ``and'' for prev word
                """
                if (-1 < _no < 100):
                    w = '%s And' % w
                """
                words.append(w)

            _no = _n
        return ' '.join(words[::-1])

    def _to_word(self, num):
        if num < 1:
            return 0, ['Zero']
        word = []
        hun = num / 100
        if hun:
            word += [self.e10[hun], self.others[100]]
        n = num % 100
        if n < 1:
            return num, word
        elif n < 10:
            """
            if word:
                word.append('And')
            """
            word.append(self.e10[n])
            return num, word
        elif n < 21:
            return num, word + [self.e20[n-10]]
        else:
            tens = n / 10
            ones = n % 10
            word.append(self.e100[tens])
            if ones:
                word.append(self.e10[ones])
            return num, word



if __name__ == '__main__':
    s = Solution()
    print s.numberToWords(int(sys.argv[1]))
