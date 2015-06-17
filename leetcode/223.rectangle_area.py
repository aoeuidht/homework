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
        x_left = max(A, E)
        x_right = min(C, G)
        y_bottom = max(B, F)
        y_top = min(D, H)
        area0 = (C - A) * (D - B)
        area1 = (G - E) * (H - F)

        overlap = 0
        if (x_left < x_right) and (y_bottom < y_top):
            overlap = (x_right - x_left) * (y_top - y_bottom)
        return area0 + area1 - overlap

if __name__ == '__main__':
    s = Solution()
    print s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
