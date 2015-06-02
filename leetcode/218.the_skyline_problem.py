#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        rst = []
        bl = len(buildings)
        if bl == 1:
            b = buildings[0]
            rst = [[b[0], b[2]],
                   [b[1], 0]]
        else:
            bs = buildings[:]
            while bs:
                bl = len(bs)
                if bl == 1:
                    rst.append([bs[0][0], bs[0][2]])
                    rst.append([bs[0][1], 0])
                    break
                slist, blist = self.merge_two(bs[0], bs[1])
                if slist:
                    rst.extend(slist)
                bs = blist + bs[2:]
                # sort bs by x satrt
                bs.sort(key=lambda i: i[0])
                #bs = sorted(blist + bs[2:], key=lambda i: i[0])

        return rst

    # return the skyline LIST, and the new building LIST
    def merge_two(self, b1, b2):
        b1l, b1h, h1 = b1
        b2l, b2h, h2 = b2

        # if they start together, split them
        if b1l == b2l:
            if b1h == b2h:
                return (None,
                        [[b1l, b1h, max(h1, h2)]])
            if b1h > b2h:
                return (None,
                        [[b1l, b2h, max(h1, h2)],
                         [b2h, b1h, h1]])
            else:
                return (None,
                        [[b1l, b1h, max(h1, h2)],
                         [b1h, b2h, h2]])

        # not connected, just yield a result
        if b2l > b1h:
            return ([(b1l, h1), (b1h, 0)], [b2])

        # same height, merge only
        if h1 == h2:
            return (None, [[min(b1l, b2l),
                            max(b1h, b2h),
                            h1]])

        # the other
        if b2h >= b1h:

            # out, right bigger
            if h1 < h2:
                return ([(b1l, h1)], [b2])
            # out, right smaller
            else:
                return ([(b1l, h1)], [[b1h, b2h, h2]])
        # the in
        else:
            # in, inner bigger
            if h1 < h2:
                return ([(b1l, h1)],
                        [b2, [b2h, b1h, h1]])
            # in, inner smaller
            else:
                return (None, [b1])

if __name__ == '__main__':
    s = Solution()
    print s.getSkyline([[2, 9, 10],
                        [3, 7, 15],
                        [5, 12, 12],
                        [15, 20, 10],
                        [19, 24, 8]])
