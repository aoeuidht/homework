#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not (board and board[0]):
            return

        bw = len(board[0])
        bh = len(board)

        # we travel the board line by line
        # record means the status of the value in line
        # -1 means unavilable
        # 0 means its a 'x'
        # positive means the group of result
        # ord('X') = 88
        record = [0 if (ord(i) ==  88) else -1
                  for i in board[0]]

        mark_map = {}
        parallel_map = {}
        erase_set = set()
        group_count = 1
        for i in range(1, bh):
            ln = board[i]
            record[0] = 0 if (ord(ln[0]) == 88) else -1
            for j in range(1, bw-1):
                if ord(ln[j]) ==  88:
                    record[j] = 0
                    continue
                # we met an 'o'
                # pity its illagle
                if ((record[j-1] == -1) or
                    (record[j] == -1)):
                    if record[j] > 0:
                        erase_set.add(record[j])
                    if record[j-1] > 0:
                        erase_set.add(record[j-1])
                    record[j] = -1
                    continue

                # mark it a number
                if ((record[j-1] == 0) and
                    (record[j] == 0)):
                    record[j] = group_count
                    mark_map[group_count] = [(i, j)]
                    group_count += 1
                if (record[j] > 0) and (record[j-1] > 0):
                    # both available
                    if record[j] != record[j-1]:
                        self.mark_para(parallel_map, record[j], record[j-1])
                    self.mark_it(mark_map, record[j], i, j)
                elif (record[j-1] == 0):
                    self.mark_it(mark_map, record[j], i, j)
                elif (record[j] == 0):
                    record[j] = record[j-1]
                    self.mark_it(mark_map, record[j], i, j)
            # the last one in line
            if ord(board[i][bw-1]) == 88:
                continue
            if record[bw-2] > 0:
                erase_set.add(record[bw-2])
        # the last line
        for i in record:
            if i > 0:
                erase_set.add(i)
        for i in erase_set:
            self.erase_rst(mark_map, parallel_map, i)

        for idx, v in mark_map.iteritems():
            if not v:
                continue
            for i, j in v:
                board[i][j] = 'X'

    def erase_rst(self, mark_map, parallel_map, i):
        stack = [i]
        handled = set([])
        while stack:
            s = stack.pop()
            if s in handled:
                continue
            handled.add(s)
            mark_map[s] = None
            for i in parallel_map.get(s, []):
                if i in handled:
                    continue
                stack.append(i)

    def mark_it(self, mark_map, idx, i, j):
        marks = mark_map[idx]
        if marks != None:
            marks.append((i, j))

    def mark_para(self, parallel_map, i, j):
        m = parallel_map.get(i, set([]))
        m.add(j)
        parallel_map[i] = m
        m = parallel_map.get(j, set([]))
        m.add(i)
        parallel_map[j] = m


if __name__ == '__main__':
    s = Solution()
    c = ['XXXXXXXX',
         'XOOXOOOX',
         'XXOXXXOX',
         'XOOOXXOX',
         'XXXOOOOX',
         'XXXXXXXX',
         'XXXXXXXX',
         'XXXXXXXX',
    ]
    c = ["XOXOXO","OXOXOX","XOXOXO","OXOXOX"]
    c = ["OXOOOOOOO","OOOXOOOOX","OXOXOOOOX","OOOOXOOOO","XOOOOOOOX","XXOOXOXOX","OOOXOOOOO","OOOXOOOOO","OOOOOXXOO"]
    c = ["XOXOOOO","XOOOOOO","XOOOOXO","OOOOXOX","OXOOOOO","OOOOOOO","OXOOOOO"]
    cand = [list(i) for i in c]
    for i in cand:
        print ''.join(i)
    print '-' * 40
    s.solve(cand)
    for i in cand:
        print ''.join(i)
