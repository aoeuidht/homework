#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    def __init__(self):
        self.bw = 0
        self.bh = 0
        self.wl = 0
        self.board = []
        self.word = None

    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if not (board and word):
            return False

        self.bw = len(board[0])
        self.bh = len(board)
        self.wl = len(word)
        self.word = word
        for l in board:
            self.board.append(list(l))
        c = word[0]
        for i in range(self.bh):
            for j in range(self.bw):
                if self.board[i][j] == c:
                    self.board[i][j] = None
                    r = self.search(i, j, 1)
                    self.board[i][j] = c
                    if r:
                        return r
        return False

    # line, column, index, direction
    # l, c: the previously matched char
    # i: the next index of word
    def search(self, l, c, i):
        if self.wl == i:
            return True

        for _l, _c in ((l, c+1), (l, c-1), (l+1, c), (l-1, c)):
            if ((0 <= _l < self.bh) and
                (0 <= _c < self.bw)):
                __c = self.board[_l][_c]
                if (__c == None) or (__c != self.word[i]):
                    continue
                self.board[_l][_c] = None
                r = self.search(_l, _c, i+1)
                self.board[_l][_c] = __c
                if r:
                    return r
        return False

if __name__ == '__main__':
    s = Solution()
    r = s.exist(["ABCE",
                 "SFCS",
                 "ADEE"],
                 'ABCB')
    print r
