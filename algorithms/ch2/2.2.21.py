#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random

import helper as hp

def find_common(n0, n1, n2):
    """
    """
    v0, v1, v2 = map(lambda i: i.next(),
                     (n0, n1, n2))
    try:
        while True:
            if v0 == v1 == v2:
                return v0
            if (v0 < v1) or (v0 < v2):
                v0 = n0.next()
            if (v1 < v0) or (v1 < v2):
                v1 = n1.next()
            if (v2 < v1) or (v2 < v0):
                v2 = n2.next()
    except:
        return None


if __name__ == '__main__':
    n0, n1, n2 = [iter(sorted([random.randint(1, 100)
                                for _ in xrange(20)]))
                  for i in (1, 2, 3)]
    rst = find_common(n0, n1, n2)
    print rst
