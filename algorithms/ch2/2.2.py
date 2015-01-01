#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random

import helper as hp

def merge_sort(items):
    aux = items[:]
    def merge(lo, mid, hi):
        print lo, mid, hi
        print items[lo:mid], items[mid+1:hi+1]
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

if __name__ == '__main__':
    items = [random.randint(1, 100) for _ in xrange(10)]
    print items
    merge_sort(items)
    print items
