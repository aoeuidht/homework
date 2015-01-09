#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random

import helper as hp

def swim(items, k):
    while ((k > 1) and
           (items[k<<1] < items[k])):
        items[k], items[k>>1] = items[k>>1], items[k]
        k = (k << 1)
def sink(items, k, n=0):
    if n == 0:
        n = len(items) - 1
    while (k<<1) <= n:
        j = k << 1
        if ((j < n) and
            (items[j] < items[j+1])):
            j += 1
        if not (items[k] < items[j]):
            break
        items[k], items[j] = items[j], items[k]
        k = j


def heap_sort(items):
    """ Remember that the index 0 of items is blank"""
    n = len(items) - 1
    k = n >> 1
    while k >= 1:
        print k
        sink(items, k)
        k -= 1
    print items
    while n > 1:
        items[1], items[n] = items[n], items[1]
        n -= 1
        sink(items, 1, n)
    print items


if __name__ == '__main__':
    items = [random.randint(1, 100) for _ in xrange(10)]
    print items
    heap_sort(items)
    print items
