#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random

import helper as hp

def insertion_sort(items, start, end):
    """

    Arguments:
    - `items`:
    """
    n = end - start + 1
    for i in range(start+1, end+1):
        for j in range(i, start, -1):
            if items[j] < items[j-1]:
                items[j], items[j-1] = items[j-1], items[j]
            else:
                break
    return items

def merge_sort(items):
    aux = items[:]
    def merge(lo, mid, hi):
        # copy lo ... hi to aux
        if items[mid] <= items[mid+1]:
            return
        aux[lo:mid+1] = items[lo:mid+1]
        # copy the right half in decreasing order
        aux[mid+1:hi+1] = items[mid+1:hi+1][::-1]
        head, tail = lo, hi
        for k in range(lo, hi+1):
            if aux[head] < aux[tail]:
                items[k] = aux[head]
                head += 1
            else:
                items[k] = aux[tail]
                tail -= 1
    def merge_sort_wrapper(lo, hi):
        if hi <= lo:
            return
        # use insertion sort for omall pieces
        if (hi - lo) < 5:
            insertion_sort(items, lo, hi)
            return
        mid = (lo + hi) / 2
        merge_sort_wrapper(lo, mid)
        merge_sort_wrapper(mid+1, hi)
        merge(lo, mid, hi)
    merge_sort_wrapper(0, len(items) - 1)

if __name__ == '__main__':
    items = [random.randint(1, 1000) for _ in xrange(20)]
    print items
    merge_sort(items)
    print items
