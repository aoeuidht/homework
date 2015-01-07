#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random

import helper as hp

def partition_fast(items, lo, hi):
    piv = items[lo]
    sp, bp = lo, hi+1
    sep, bep = lo, hi+1
    while True:
        while True:
            sp += 1
            item = items[sp]
            if item < piv:
                if sp == hi:
                    sp += 1
                    break
            elif item == piv:
                sep += 1
                items[sep], items[sp] = items[sp], items[sep]
                if sp == hi:
                    sp += 1
                    break
            else:
                break
        while True:
            bp -= 1
            item = items[bp]
            if piv < item:
                if bp == lo:
                    break
            elif item == piv:
                if bp == lo:
                    break
                bep -= 1
                items[bep], items[bp] = items[bp], items[bep]
            else:
                break
        if sp >= bp:
            break
        items[sp], items[bp] = items[bp], items[sp]
    #print sp, bp, sep, bep
    for idx in range(lo, sep+1):
        near, far = idx, sp-1-(idx-lo)
        items[near], items[far] = items[far], items[near]
    for idx in range(bep, hi+1):
        near = idx-bep+bp+1
        far = idx
        items[near], items[far] = items[far], items[near]
    return sp-1-sep+lo, hi-bep+bp+1

def quick_sort(items, lo, hi):
    #print lo, hi, items
    if hi <= lo:
        return
    i, j = partition_fast(items, lo, hi)
    if lo < i:
        quick_sort(items, lo, i-1)
    if hi > j:
        quick_sort(items, j+1, hi)


if __name__ == '__main__':
    for i in range(1000):
        items = [random.randint(1, 10) for _ in xrange(100)]
        s = sorted(items)
        quick_sort(items, 0, len(items)-1)
        print s == items
