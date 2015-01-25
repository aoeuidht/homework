#!/usr/bin/env python
# -*- coding: utf-8 -*-

import graph

class BreadthFirstPaths:
    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.marked = set()

    def dist_to(self, v):
        # the queue for the vertex list
        return dist_to_wrapper(self.s, v, 0)


    def dist_to_wrapper(self, s, v, depth):
        vertex_queue = [(s, 0)]
        while vertex_queue:
            s, depth = vertex_queue.pop(0)
            self.marked.add(s)
            for _s in self.g.adj(s):
                if _s in self.marked:
                    continue
                # add them to the queue
                self.marked.add(_s)
                # check if target
                if _s == v:
                    return depth + 1
                self.vertex_queue.append((_s, depth+1))
