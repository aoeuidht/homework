#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from oj_helper import *

from collections import deque

class Solution:
    # initialize your data structure here.
    def __init__(self):
        self.qs = deque()
        self.q = deque()
        self.max_item_num = 10

    # @param x, an integer
    # @return nothing
    def push(self, x):
        qlen = len(self.q)
        if qlen >= self.max_item_num:
            self.qs.append(self.q)
            self.q = deque()
        self.q.append(x)

    # @return nothing
    def pop(self):
        self.q.reverse()
        r = self.q.popleft()
        self.q.reverse()
        #
        if (len(self.q) < 1) and self.qs:
            print 'oops, start to pop from the qs'
            self.qs.reverse()
            self.q  = self.qs.popleft()
            self.qs.reverse()
        return r

    # @return an integer
    def top(self):
        self.q.reverse()
        r = self.q[0]
        self.q.reverse()
        return r

    # @return an boolean
    def empty(self):
        return (len(self.q) + len(self.qs)) < 1


if __name__ == '__main__':
    s = Solution()
    for i in range(1000):
        s.push(i)
        if (i % 2) == 0:
            print s.pop()

    while not s.empty():
        print s.pop()
