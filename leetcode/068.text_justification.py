#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        r = []
        # every item in i is a tuple: (total_len, word_count, word_list)
        _i = [0, 0, []]
        for i in words:
            wl = len(i)
            if (_i[0] + _i[1] + wl) <= L:
                _i[0] += wl
                _i[1] += 1
                _i[2].append(i)
            else:
                r.append(_i)
                _i = [wl, 1, [i]]
        if _i[1] > 0:
            r.append(_i)

        if not r:
            return []
        rst = [self.massage_rst(_r, L) for _r in r[:-1]]
        rst.append(' '.join(r[-1][2]) + ' ' * (L - r[-1][0] - r[-1][1] + 1))
        return rst

    def massage_rst(self, cand, L):
        sl, sc, words = cand
        if sc == 1:
            return '%s%s' % (words[0], ' ' * (L - sl))
        step = (L - sl) / (sc - 1)
        remainder = L - sl -  (sc - 1) * step
        rst = [words[0]]
        for w in words[1:]:
            rst.append(' ' * (step + (1 if remainder > 0 else 0)))
            rst.append(w)
            remainder -= 1
        return ''.join(rst)


if __name__ == '__main__':
    s = Solution()
    print s.fullJustify(["a","b","c","d","e"], 3)
