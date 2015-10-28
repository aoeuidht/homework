#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from oj_helper import *


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not (board  and board[0]):
            return
        h, w = len(board)-1, len(board[0])-1

        buf = [0] * (w + 1)
        h_buf = [0] * (w + 1)
        for _h in range(h+1):
            # write the prev result
            h_buf = buf[:]

            # calc the resurt to buf
            for _w in range(w+1):
                # live neighbors count
                ln = 0
                # left-top
                if _h and _w:
                    ln += board[_h-1][_w-1]
                # top
                if _h:
                    ln += board[_h-1][_w]
                # right-top
                if _h and (_w < w):
                    ln += board[_h-1][_w+1]
                # left
                if _w:
                    ln += board[_h][_w-1]
                # right
                if _w < w:
                    ln += board[_h][_w+1]
                # left-bottom
                if (_h < h) and _w:
                    ln += board[_h+1][_w-1]
                # bottom
                if _h < h:
                    ln += board[_h+1][_w]
                # right-bottom
                if (_h < h) and (_w < w):
                    ln += board[_h+1][_w+1]

                print _h, _w, board[_h][_w], ln
                if board[_h][_w]:
                    if ln < 2:
                        buf[_w] = 0
                    elif ln < 4:
                        buf[_w] = 1
                    else:
                        buf[_w] = 0
                    continue
                if ln == 3:
                    buf[_w] = 1
                else:
                    buf[_w] = 0
            if _h:
                for _w in range(w+1):
                    board[_h-1][_w] = h_buf[_w]

        for _w in range(w+1):
            board[h][_w] = buf[_w]


if __name__ == '__main__':
    s = Solution()
    #b = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    b = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
    for i in b:
        print i
    s.gameOfLife(b)

    for i in b:
        print i
