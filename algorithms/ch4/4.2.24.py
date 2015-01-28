#!/usr/bin/env python

# -*- coding: utf-8 -*-

import graph

class HamiltonianPath:
    def __init__(self, dg):
        self.dg = dg
        self.order = graph.DepthFirstOredr(self.dg)

    def chk(self):
        return all(lambda pair: self.dg.has_edge(*pair),
                   zip(self.order[:-1], self.order[1:]))
