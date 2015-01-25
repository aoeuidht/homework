#!/usr/bin/env python
# -*- coding: utf-8 -*-

import graph

class G415(graph.Graph):
        def add_edge(self, v, w):
            if v == w:
                raise Exception('error-dege', 'self-edge')
            if self.has_edge(v, w):
                raise Exception('error-dege', 'parallel-edge')
            super(G415, self).add_edge(v, w)
