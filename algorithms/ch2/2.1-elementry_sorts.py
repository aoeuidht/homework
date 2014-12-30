#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random

import helper as hp


def selection_sort(items):
    """

    Arguments:
    - `list_to_sort`:
    """
    n = len(items)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if items[j] < items[min]:
                min = j
        items[i], items[min] = items[min], items[i]

def insertion_sort(items):
    """

    Arguments:
    - `items`:
    """
    n = len(items)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if items[j] < items[j-1]:
                items[j], items[j-1] = items[j-1], items[j]
            else:
                break

def compare_sort(m0, m1, arr_len, cnt):
    """

    Arguments:
    - `m0`:
    - `m1`:
    - `arr_len`:
    - `cnt`:
    """
    gl = globals()
    _m0, _m1 = gl[m0], gl[m1]
    # generate random array with length arr_len
    items = [random.random() for _ in xrange(arr_len)]

    cm0 = lambda: [_m0(items[:]) for _ in xrange(cnt)]
    cm1 = lambda: [_m1(items[:]) for _ in xrange(cnt)]

    cost_m0, _ = hp.time_calc(cm0)
    cost_m1, _ = hp.time_calc(cm1)

    print 'For %d random doubles %d times' % (arr_len, cnt)
    print '%s: %f vs %s: %f' % (m0, cost_m0, m1, cost_m1)


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print 'usage: python %s sort_method sort_method2 random-double-numbers sort-times' % sys.argv[0]
        sys.exit(0)
    m0, m1, cnt, loops = sys.argv[1:5]
    cnt = int(cnt)
    loops = int(loops)
    compare_sort(m0, m1, cnt, loops)
