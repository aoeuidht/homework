#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from oj_helper import *

from collections import deque

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.qs = deque()
        self.q = deque()
        self.que_quota = 10


    # @param x, an integer
    # @return nothing
    def push(self, x):
        qlen = len(self.q)
        if qlen >=  self.que_quota:
            self.qs.reverse()
            self.qs.append(self.q)
            self.qs.reverse()
            self.q = deque()
        self.q.append(x)

    # @return nothing
    def pop(self):
        if len(self.qs):
            q = self.qs[-1]
        else:
            q = self.q
        q.reverse()
        r = q.pop()
        q.reverse()

        #
        if len(self.qs) and (len(q) < 1):
            self.qs.pop()
        return r

    # @return an integer
    def peek(self):
        if len(self.qs):
            q = self.qs[-1]
        else:
            q = self.q
        q.reverse()
        r = q[-1]
        q.reverse()
        return r

    # @return an boolean
    def empty(self):
        return (len(self.q) + len(self.qs)) < 1

if __name__ == '__main__':
    s = Queue()
    for i in range(100):
        s.push(i)
        print s.qs, s.q
        if (i % 2) == 0:
            print s.peek(), s.pop()

    while not s.empty():
        print s.peek(), s.pop()
