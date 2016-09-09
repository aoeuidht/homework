#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from oj_helper import *

class Solution(object):
    def __init__(self):
        """

        Arguments:
        - `self`:
        """
        self.rsts = set()
        self.rm_cnt = 0
        self.s = ''
        self.l = 0

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.s = s
        self.l = len(s)
        self.rm_cnt = self.l + 1
        if not s:
            return ['']
        self.rmpar('', 0, 0, 0)
        if not self.rsts:
            self.rsts.add('')
        return list(self.rsts)

    def add_rst(self, rm_cnt, rst):
        """

        Arguments:
        - `self`:
        - `rm_rnt`:
        - `rst`:
        """
        if rm_cnt < self.rm_cnt:
            self.rm_cnt = rm_cnt
            self.rsts = set()
            self.rsts.add(rst)
        elif rm_cnt == self.rm_cnt:
            self.rsts.add(rst)

    def validate(self, start, left_cnt):
        """

        Arguments:
        - `self`:
        - `start`:
        - `left_cnt`:
        """
        for i in range(start, self.l):
            cur = self.s[i]
            if cur == '(':
                left_cnt += 1
            elif cur == ')':
                left_cnt -= 1
            if left_cnt < 0:
                return False
        if left_cnt <> 0:
            return False
        return True

    def rmpar(self, prev_str, start, left_cnt, rm_cnt):
        """
        """
        if rm_cnt > self.rm_cnt:
            return
        prev_char = prev_str[-1] if prev_str else ''
        next_char = self.s[start]
        full_str = '%s%s' % (prev_str, next_char)
        if start == self.l - 1:
            if next_char == ')':
                if (left_cnt ==  1):
                    # gotcha
                    self.add_rst(rm_cnt, full_str)
                elif left_cnt == 0:
                    self.add_rst(rm_cnt + 1, prev_str)
            elif next_char == '(':
                if left_cnt == 0:
                    self.add_rst(rm_cnt + 1, prev_str)
            else:
                if left_cnt == 0:
                    self.add_rst(rm_cnt, full_str)
            return


        # fast skip
        if self.validate(start, left_cnt):
            self.add_rst(rm_cnt, '%s%s' % (prev_str, self.s[start:]))
            return

        if next_char == '(':
            self.rmpar(full_str, start + 1, left_cnt + 1, rm_cnt)
            # delete
            self.rmpar(prev_str, start + 1, left_cnt, rm_cnt + 1)
        elif next_char == ')':
            if left_cnt > 0:
                # got right, reduce the left cnt
                self.rmpar(full_str, start + 1, left_cnt - 1, rm_cnt)
            # delete
            self.rmpar(prev_str, start + 1, left_cnt, rm_cnt + 1)
        else:
            self.rmpar(full_str, start + 1, left_cnt, rm_cnt)
            self.rmpar(prev_str, start + 1, left_cnt, rm_cnt + 1)
        return

if __name__ == '__main__':
    s = Solution()
    print s.removeInvalidParentheses('()())()')
    print s.removeInvalidParentheses('(a)())()')
    print '-----------'
    print s.removeInvalidParentheses(sys.argv[1])
