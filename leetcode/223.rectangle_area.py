#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from oj_helper import *

class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        # check if they has any overlap
        area0 = self.gen_points(A, B, C, D)
        area1 = self.gen_points(E, F, G, H)

        area0, area1 = (area0, area1) if A <= E else (area1, area0)

        a0_chk = map(lambda p: self.point_in_area(p, area1),
                     area0)
        a1_chk = map(lambda p: self.point_in_area(p, area0),
                     area1)

        area0 = (C - A) * (D - B)
        area1 = (G - E) * (H - F)
        if (not any(a0_chk)) and (not any(a1_chk)):
            # a + b
            return area0 + area1
        elif ((not any(a0_chk)) and all(a1_chk)):
            return area0
        elif ((not any(a1_chk)) and all(a0_chk)):
            return area1
        # here the most complex case


    def point_in_area(point, area):
        x, y = point
        x0, y0 = area[0]
        x1, y1 = area[2]
        return (x0 <= x <= x1) and (y0 <= y <= y1)

    def gen_points(self, A, B, C, D):
        # return left-bottom, right-bottom, right-top, left-top
        # points with format (x, y)
        return ((A, B), (C, B), (C, D), (A, D))

if __name__ == '__main__':
    s = Solution()
