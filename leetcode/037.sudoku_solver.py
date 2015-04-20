#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from oj_helper import *

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.

    def solveSudoku(self, board):
        self.s_wrapper(board)

    def s_wrapper(self, board):
        row_set, line_set, cubic_set = self.anal_board(board)
        full_set = set(list('123456789'))
        chk = True
        cand_map = {}
        while chk:
            chk = False
            gotcha = False
            for i, j in [(i, j) for i in range(9) for j in range(9)]:
                v = board[i][j]
                if v != '.':
                    continue
                chk = True
                row, line, cubic = self.get_idx(i, j)
                r = row_set[row].union(line_set[line], cubic_set[cubic])
                cands = full_set - r
                cl = len(cands)
                if cl == 0:
                    # error happens
                    return False
                if cl == 1:
                    gotcha = True
                    _v = cands.pop()
                    board[i][j] = _v
                    row_set[row].add(_v)
                    line_set[line].add(_v)
                    cubic_set[cubic].add(_v)
                else:
                    cand_map[i*9+j] = cands
            if not gotcha:
                break
        #print cand_map
        if not cand_map:
            return True
        idx, cands, cl = None, None, 1000
        for k, v in cand_map.iteritems():
            vl = len(v)
            if vl < cl:
                idx, cands, cl = k, v, vl
        row = idx / 9
        line = idx % 9
        # copy the board
        r = False
        for _c in cands:
            b = [_b[:] for _b in board]

            # assign a value
            b[row][line] = _c
            r = self.s_wrapper(b)
            if r:
                # check b
                row_set, line_set, cubic_set = self.anal_board(b)
                if any(map(lambda s: len(s) < 9,
                           row_set + line_set + cubic_set)):
                    r = False
                    continue
                for i, j in [(i, j)
                             for i in range(9)
                             for j in range(9)]:
                    board[i][j] = b[i][j]
                break
        return r

    def get_idx(self, i, j):
        # return line, column, cubic
        return i, j, i/3*3+j/3

    def get_item_by_idx(self, i, j):
        return [[(i, k) for k in range(9)],
                [(k, j) for k in range(9)],
                [(_i, _j) for _i in range(i/3*3, i/3*4)
                 for _j in range(j/3*3, j/3*4)]]

    def anal_board(self, board):
        row_set = [set() for i in range(9)]
        line_set = [set() for i in range(9)]
        cubic_set = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                idx = i * 9 + j
                v = board[i][j]
                if v != '.':
                    row, line, cubic = self.get_idx(i, j)
                    row_set[row].add(v)
                    line_set[line].add(v)
                    cubic_set[cubic].add(v)
        return row_set, line_set, cubic_set


    def pb(self, b, bt):
        print '-------- ', bt, ' board here ---------'
        for l in b:
            print ''.join(l)

if __name__ == '__main__':
    sys.setrecursionlimit(25)
    s = Solution()
    mat = ['53..7....',
           '6..195...',
           '.98....6.',
           '8...6...6',
           '4..8.3..1',
           '7...2...6',
           '.6....28.',
           '...419..5',
           '....8..79']
    mat = ["..9748...",
           "7........",
           ".2.1.9...",
           "..7...24.",
           ".64.1.59.",
           ".98...3..",
           "...8.3.2.",
           "........6",
           "...2759.."]
    mat = ["53..7....",
           "6..195...",
           ".98....6.",
           "8...6...3",
           "4..8.3..1",
           "7...2...6",
           ".6....28.",
           "...419..5",
           "....8..79"]
    m = []
    for _m in mat:
        m.append(list(_m))

    s.solveSudoku(m)
    for _m in m:
        print ''.join(_m)
