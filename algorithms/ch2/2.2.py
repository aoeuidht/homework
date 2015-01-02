#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random

import helper as hp

def merge_sort(items):
    aux = items[:]
    def merge(lo, mid, hi):
        i, j = lo, mid+1
        # copy lo ... hi to aux
        aux[lo:hi+1] = items[lo:hi+1]
        for k in range(lo, hi+1):
            if i > mid:
                items[k] = aux[j]
                j += 1
            elif j > hi:
                items[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                items[k] = aux[j]
                j += 1
            else:
                items[k] = aux[i]
                i += 1
    def merge_sort_wrapper(lo, hi):
        if hi <= lo:
            return
        mid = (lo + hi) / 2
        merge_sort_wrapper(lo, mid)
        merge_sort_wrapper(mid+1, hi)
        merge(lo, mid, hi)
    merge_sort_wrapper(0, len(items) - 1)

def mergebu_sort(items):
    aux = items[:]
    def merge(lo, mid, hi):
        i, j = lo, mid+1
        # copy lo ... hi to aux
        aux[lo:hi+1] = items[lo:hi+1]
        for k in range(lo, hi+1):
            if i > mid:
                items[k] = aux[j]
                j += 1
            elif j > hi:
                items[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                items[k] = aux[j]
                j += 1
            else:
                items[k] = aux[i]
                i += 1
    sz = 1
    n = len(items)
    while sz < n:
        for lo in range(0, n-sz, sz*2):
            merge(lo, lo+sz-1, (n-1) if (lo+sz+sz > n) else (lo+sz+sz-1))
        sz *= 2

if __name__ == '__main__':
    items = [random.randint(1, 100) for _ in xrange(10)]
    print items
    mergebu_sort(items)
    print items
