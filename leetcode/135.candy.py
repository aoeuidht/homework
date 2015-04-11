#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        l = len(ratings)
        if l == 0:
            return 0
        elif l == 1:
            return 1

        # first element means index
        # the 2nd 1: bigger than neighbor, -1 means smaller
        stack = []

        rts = ratings
        # 1st
        if rts[0] <= rts[1]:
            stack.append((0, -1))
        else:
            stack.append((0, 1))

        for i in range(1, l-1):
            v = rts[i]
            if ((rts[i-1] >= v) and
                (v <= rts[i+1])):
                stack.append((i, -1))
                continue
            if ((rts[i-1] <= v) and
                (v >= rts[i+1])):
                stack.append((i, 1))
        # the last
        if rts[l-1] > rts[l-2]:
            stack.append((l-1, 1))
        else:
            stack.append((l-1, -1))

        # now handle the stack
        #print stack
        cc = [-1] * l
        while stack:
            idx, tp = stack.pop()
            if not stack:
                if tp < 0:
                    cc[idx] = cc[idx] if (cc[idx] > 0) else 1
                else:
                    cc[idx] = cc[idx+1] + 1
                break

            if tp < 0:
                cc[idx] = 1
                _idx, _ = stack[-1]

                for i in range(idx-1, _idx, -1):
                    cc[i] = cc[i+1] + 1
            else:
                _idx, _ = stack[-1]
                for i in range(_idx+1, idx+1):
                    cc[i] = i - _idx + 1
                if idx < (l-1):
                    if rts[idx] != rts[idx+1]:
                        cc[idx] = max(cc[idx-1], cc[idx+1]) + 1
        _i = 0
        for i, j in zip(rts, cc):
            print i, j, ('<---------' if _i == i else '')
            _i = i
        return sum(cc)

if __name__ == '__main__':
    s = Solution()
    r = s.candy([1, 2, 4, 4, 3])
    print r
    r = s.candy([29, 51, 87, 87, 72, 12])
    print r
    r = s.candy([58,21,72,77,48,9,38,71,68,77,82,47,25,94,89,54,26,54,54,99,64,71,76,63,81,82,60,64,29,51,87,87,72,12,16,20,21,54,43,41,83,77,41,61,72,82,15,50,36,69,49,53,92,77,16,73,12,28,37,41,79,25,80,3,37,48,23,10,55,19,51,38,96,92,99,68,75,14,18,63,35,19,68,28,49,36,53,61,64,91,2,43,68,34,46,57,82,22,67,89])
    print r
    r = s.candy(map(int, sys.argv[1].split(',')))
    print r
