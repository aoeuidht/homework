#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random

import helper as hp

def insertion_sort(start, end,
                   get_index_of,
                   comp, exchange):
    n = end - start + 1
    for i in range(start+1, end+1):
        for j in range(i, start, -1):
            item_j = get_index_of(j)
            item_j_m1 = get_index_of(j-1)
            if comp(item_j, item_j_m1) < 0:
                exchange(j, j-1)
            else:
                break

def merge(items, aux, lo, mid, hi):
    """

    Arguments:
    - `items`: items to be merged
    - `aux`: the auxiliary array
    """
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

def merge_sort(items, m):
    """

    Arguments:
    - `m`: the length of sub blocks, the length of items should be a multiple of M
    """
    aux = items[:]
    n = len(items)
    def natual_gen():
        start = 0
        prev_value = items[0]
        for i in range(1, n):
            if items[i] < prev_value:
                yield (start, i-1)
                start = i
            prev_value = items[i]
        yield start, n - 1

    while True:
        lo = hi = None
        for p in natual_gen():
            if (p[0] == 0 and p[1] == (n - 1)):
                return
            if lo is None:
                lo = p
            else:
                hi = p
                merge(items, aux, lo[0], lo[1], hi[1])
                lo = hi = None

if __name__ == '__main__':
    items = [random.randint(1, 100) for _ in xrange(20)]
    print items
    m = 5
    merge_sort(items, m)
    print items
