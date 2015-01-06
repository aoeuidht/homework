#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random

import helper as hp

def partition(items, lo, hi):
    i, j = lo, hi+1
    piv = items[lo]
    while True:
        while True:
            i += 1
            if items[i] < piv:
                if i == hi:
                    break
            else:
                break
        while True:
            j -= 1
            if piv < items[j]:
                if j == lo:
                    break
            else:
                break
        if i >= j:
            break
        items[i], items[j] = items[j], items[i]
    items[lo], items[j] = items[j], items[lo]
    return j

def quick_sort(items, lo, hi):
    if hi <= lo:
        return
    j = partition(items, lo, hi)
    quick_sort(items, lo, j-1)
    quick_sort(items, j+1, hi)

def quick_part(item, lo, hi):
    pass

if __name__ == '__main__':
    items = [random.randint(1, 100) for _ in xrange(10)]
    print items
    quick3_sort(items, 0, len(items)-1)
    print items
