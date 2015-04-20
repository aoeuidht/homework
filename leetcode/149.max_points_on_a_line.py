#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from oj_helper import *

"""
"""
class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        pl = len(points)
        if pl == 1:
            return 1

        rst = 0
        for i in range(0, pl):
            tg_map = {}
            self_cnt = 1
            c = 0
            for j in range(i+1, pl):
                ptg = self.calc_tg(points[i], points[j], pl)
                if not ptg:
                    self_cnt += 1
                else:
                    _c = tg_map.get(ptg, 0) + 1
                    tg_map[ptg] = _c
                    if _c > c:
                        c = _c
            _r = self_cnt + c
            if _r > rst:
                rst = _r
        return rst

    def calc_tg(self, p0, p1, maxtg):
        if ((p0.x == p1.x) and
            (p0.y == p1.y)):
            return None
        if p0.x == p1.x:
            return '0'
        if p0.y == p1.y:
            return '%d' % maxtg
        dx = p0.x - p1.x
        dy = p0.y - p1.y
        if dx > 0:
            sign = 1 if dy > 0 else -1
            dy *= sign
        else:
            dx = -dx
            sign = -1 if dy > 0 else -1
            dy *= -sign

        g = self.gcd(dx, dy)
        return '%d_%d' % (dx * sign / g, dy / g)

    def gcd(self, x, y):
        while y != 0:
            x, y = y, x % y
        return x

if __name__ == '__main__':
    s = Solution()
    cands = [Point(1, 1), Point(1, 1), Point(1, 1)]
    print s.maxPoints(cands)
