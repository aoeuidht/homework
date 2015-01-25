#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Graph:
    def __init__(self):
        # the count of vertices and edges
        self.vc = 0
        self.ec = 0

        #the dict used for vertices and edges
        self.graph = {}

    def adj(self, v):
        return self.graph.get(v, [])

    def add_edge(self, v, w):
        self.graph.setdefault(v, [])
        self.graph.setdefault(w, [])
        self.graph[v].append(w)
        self.graph[w].append(v)
        self.vc += 2

    def has_edge(self, v, w):
        return w in self.graph.get(v, [])

    def from_file(self, fn):
        skip = 2
        with open(fn) as f:
            for ln in f.readlines():
                if skip:
                    skip -= 1
                    continue
                v, s = map(lambda v: int(v),
                           ln.split())
                self.add_edge(v, s)

class Digraph(Graph):
    def add_edge(self, v, w):
        self.graph.setdefault(v, [])
        self.graph[v].append(w)
        self.vc += 1
        if len(self.graph[v]) == 1:
            self.ec += 1

    def reverse(self):
        r = Digraph()
        for v in self.graph.keys():
            for w in self.graph[v]:
                r.add_edge(w, v)
        return r

class DepthFirstOredr():
    def __init__(self, dg):
        self.dg = dg
        self.marked = set()
        self._pre = []
        self._post = []
        # we should use reverse post as a queue
        self._reverse_post = []

    def go(self):
        vertices = self.dg.graph.keys()
        vertices.sort()
        for v in vertices:
            if v in self.marked:
                continue
            self.dfs(v)

    def dfs(self, v):
        self._pre.append(v)
        self.marked.add(v)
        for w in self.dg.adj(v):
            if w in self.marked:
                continue
            self.dfs(w)
        self._post.append(v)
        self._reverse_post.append(v)

    def pre(self):
        if not self._pre:
            self.go()
        return self._pre

    def post(self):
        if not self._post:
            self.go()
        return self._post

    def reverse_post(self):
        if not self._reverse_post:
            self.go()
        return self._reverse_post[::-1]

class KosarajuSCC:
    def __init__(self, dg):
        self.dg = dg

        self.count = 0
        self.ids = {}
        self.marked = set()

    def go(self):
        order = DepthFirstOredr(self.dg.reverse())
        order.go()
        for s in order.reverse_post():
            if s in self.marked:
                continue
            self.dfs(s)
            self.count += 1

    def dfs(self, v):
        self.marked.add(v)
        self.ids[v] = self.count

        for w in self.dg.adj(v):
            if w in self.marked:
                continue
            self.dfs(w)

    def strongly_connected(self, w, v):
        return self.ids[v] == self.ids[w]

    def vertex_id(self, v):
        return self.ids[v]

    def c_count(self):
        return self.count

if __name__ == '__main__':
    dg_data = sys.argv[1]
    dg = Digraph()
    dg.from_file(dg_data)

    kscc = KosarajuSCC(dg)
    kscc.go()

    print kscc.ids
    print kscc.count
