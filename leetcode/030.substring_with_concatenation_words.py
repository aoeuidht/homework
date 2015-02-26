#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""

class Solution:
    def gen_item_dict(self, L):
        rst = {}
        for i in L:
            _i = rst.get(i, [1])
            _i.append(-1)
            rst[i] = _i
        return rst

    def fwrapper(self, S, lo, hi, L, item_len):
        # we find every 3 characters
        ld = None
        llen = len(L)
        if (hi - lo + 1) < (llen * item_len):
            return []
        # string hit
        hl = 0
        r = lo
        rst = []
        lset = set(L)
        for i in range(lo, hi-item_len+1, item_len):
            niddle = S[i:i+item_len]
            #print 'calc ', i, ' now, got ', niddle, ' here'
            if niddle in lset:
                if not ld:
                    ld = self.gen_item_dict(L)
                # check the holes are full
                hit_info = ld[niddle]
                hit_pos = hit_info[0]
                if hit_pos >= len(hit_info):
                    # the holes are full, so we'll have to roll back
                    dup_pos = min(hit_info[1:])
                    for j in range(r, dup_pos + 1, item_len):
                        _n = S[j:j+item_len]
                        _hi = ld[_n]
                        hp = _hi[0]
                        if _hi[hp-1] != j:
                            # swap with the last one, then decrease the offset
                            for _i in range(1, len(_hi)-1):
                                if _hi[_i] == j:
                                    _hi[_i], _hi[hp-1] = _hi[hp-1], _hi[_i]
                        _hi[0] = hp -1
                        hl -= 1
                    r = dup_pos + item_len
                    hit_pos -= 1

                hl += 1
                hit_info[hit_pos] = i
                hit_info[0] += 1
                r = i if (hl ==  1) else r
                if hl == llen:
                    rst.append(r)
            else:
                # if a 3-character string not in list, we start again
                if (hi - lo + 1) < (llen * item_len):
                    break
                ld = None
                hl = 0
        return rst
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        if not L:
            return []
        slen = len(S)
        item_len = len(L[0])
        return reduce(lambda l, r: l+r,
                      map(lambda i: self.fwrapper(S, i, slen, L, item_len),
                          range(item_len)))

if __name__ == '__main__':
    s = Solution()
    print s.findSubstring(sys.argv[1], sys.argv[2].split(','))
