#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, adict):
        if start == end:
            return 0
        rst = []

        if end in adict:
            adict.remove(end)
        # the dist, parent-list
        stack = [[end, None]]
        lo, hi = 0, 0
        n_stack = []
        while hi >= lo:
            # check if we met the result
            for i in range(lo, hi+1):
                c = stack[i][0]
                if self.one_diff(c, start):
                    # push result to rst
                    rst += self.gen_rst(stack, i, [start])
                    return len(rst[0])
            if rst:
                return rst

            _hi = hi

            nd = {}
            for i in range(lo, hi+1):
                s = list(stack[i][0])
                # loop for all possiblility
                for j in range(len(s)):
                    _c = s[j]
                    for __c in 'abcdefghijklmnopqrstuvwxyz':
                        if __c == _c:
                            continue
                        s[j] = __c
                        t = ''.join(s)
                        if t in adict:
                            _r = nd.get(t, [])
                            _r.append(i)
                            nd[t] = _r
                    s[j] = _c
            for k in nd.keys():
                stack.append([k, nd[k]])
                adict.remove(k)
                _hi += 1
            lo, hi = hi + 1, _hi
        return rst

    def gen_rst(self, stack, idx, rst_pre):
        r = rst_pre[:]
        c, parents = stack[idx]
        r.append(c)
        if not parents:
            return [r]
        rst = []
        for _idx in parents:
            rst += self.gen_rst(stack, _idx, r)
        return rst

    def one_diff(self, c, s):
        _c = 0
        for i in range(len(s)):
            _c += (1 if (c[i] != s[i]) else 0)
        return _c == 1

if __name__ == '__main__':
    sys.setrecursionlimit(25)
    s = Solution()
    r = s.findLadders('hit', 'cog', set(["hot","dot","dog","lot","log"]))
    print r
    cand = set(open('126.test.txt').read()[:-1].split(','))
    r = s.findLadders( "nanny", "aloud", cand)
    r = s.findLadders('hot', 'dog', ['hot', 'dog', 'dot'])
    print r
