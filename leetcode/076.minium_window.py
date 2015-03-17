#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    def __init__(self):
        self.td = {}
        self.cd = []
        self.t = []
        self.tl = 0

    def swap_char(self, i0, i1):
        self.t[i0], self.t[i1] = self.t[i1], self.t[i0]
        c0, c1 = self.cd[i0], self.cd[i1]
        self.cd[i0], self.cd[i1] = c1, c0
        self.td[c0], self.td[c1] = self.td[c1], self.td[c0]

    def sink_heap(self, c):
        o = self.td[c]
        tl = len(self.t)
        # sink
        while True:
            s0 = o * 2 + 1
            s1 = s0 + 1
            sidx = -1
            if s0 >= tl:
                return
            elif s1 >= tl:
                sidx = s0
            else:
                sidx = s0 if (self.t[s0] > self.t[s1]) else s1
            if (sidx >= 0) and (self.t[o] < self.t[sidx]):
                self.swap_char(o, sidx)
                o = sidx
            else:
                break

    def pop_heap(self, c):
        o = self.td[c]
        if o < 1:
            return
        # sink
        while True:
            to = (o - 1) / 2
            if self.t[o] > self.t[to]:
                self.swap_char(o, to)
            else:
                break
            o = to
            if o < 1:
                break

    def dec_char_count(self, c, pos=-1):
        idx = self.td.get(c, -1)
        if idx < 0:
            return -1
        self.t[idx] += pos
        return idx

    # @return a string
    def minWindow(self, S, T):
        if not (S and T):
            return ''
        if len(T) > len(S):
            return ''

        self.tl = len(T)

        td = {}
        for i, j in enumerate(list(T)):
            r = td.get(j, 0)
            r += 1
            td[j] = r
        c = [(i, j) for i, j in td.iteritems()]
        c = sorted(c, key=lambda _c: -_c[1])
        for idx, c_num in enumerate(c):
            _c, num = c_num
            self.td[_c] = idx
            self.cd.append(_c)
            self.t.append(num)

        # t is a maxmium heap

        rlo, rhi = -1, -1
        lo = hi = l = -1
        i = -1
        print zip(self.cd, self.t)
        for c in S:
            i += 1
            #dec the counter
            char_idx = self.dec_char_count(c)
            if char_idx < 0:
                continue
            else:
                self.sink_heap(c)
                lo = lo if (lo > -1) else i

            #print zip(self.cd, self.t), S[i:]
            if self.t[0] == 0:
                print 'self.t is', self.t
                hi = i
                _l = hi - lo + 1
                if (l < 0) or (_l < l):
                    print 'we set it here', zip(self.cd, self.t), S[lo:hi+1]
                    rlo, rhi, l = lo, hi, _l
                if l == self.tl:
                    break
                # pop until not match others
                print 'start to nian from', S[lo:hi+1]
                s_invalid = False
                for p in range(lo, hi+1):
                    lo += 1
                    _c = S[p]
                    if self.td.has_key(_c):
                        if self.t[0] > 0:
                            lo -= 1
                            print 'invalid', S[lo:hi+1]
                            break
                        self.dec_char_count(_c, 1)
                        self.pop_heap(_c)
                        print zip(self.cd, self.t), S[lo:]
                        # check if it still works
                    if self.t[0] < 1:
                        _l = hi - lo + 1
                        if (l < 0) or (_l < l):
                            print 'shorted from', S[lo-1:hi+1], 'to', S[lo:hi+1]
                            rlo, rhi, l = lo, hi, _l
        print rlo, rhi
        if l > 0:
            return S[rlo:rhi+1]
        return ''

if __name__ == '__main__':
    """
    s = Solution()
    print s.minWindow('aaaaaab', 'aab')
    s = Solution()
    print s.minWindow('bdab', 'ab')
    s = Solution()
    print s.minWindow('bdab', 'a')
    s = Solution()
    print s.minWindow('ask_not_what_your_country_can_do_for_you_ask_what_you_can_do_for_your_country', 'ask_country')
    s = Solution()
    print s.minWindow('zechiwcmjktroasetkzxlxpdibkeiqdhuhqfdsrmfmfvny', 'ziiahux')
    s = Solution()
    print s.minWindow('oordodnkiwpuajhabhuuegupzfksiziwqcbgfospkhjmqrptajogrivtnhlyjwubywhfmcvzjglcx', 'avamlidugyjnmhyieziajp')
    """
    s = Solution()
    print s.minWindow('fqqhcjlvvbxjliqttcmzcnidizbjbjajbsqeddbyhykshalcczegnojxnmirykazcsffwggdfqxosiqxiwdxkpuadfrbptbulibjphowzlksucpezubllxlpcesuxvolerutbjpaubuqdl',
                      'uegvqttbi')
    print 'heheh'
