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
    def merge_sort_wrapper(lo, hi):
        if hi <= lo:
            return
        mid = (lo + hi) / 2
        merge_sort_wrapper(lo, mid)
        merge_sort_wrapper(mid+1, hi)
        merge(items, aux, lo, mid, hi)
    #merge_sort_wrapper(0, len(items) - 1)
    n = len(items)
    # 1. sort the blocks itself
    def exchange(i, j):
        items[i], items[j] = items[j], items[i]
    for i in range(0, n, m):
        insertion_sort(i, i+m-1,
                       lambda k: items[k],
                       lambda i, j: -1 if (i < j) else 1,
                       exchange)
    # 2. sort the bolcks by the 1st element as key
    def exchange_batch(i, j):
        items[i*m:(i+1)*m], items[j*m:(j+1)*m] = items[j*m:(j+1)*m], items[i*m:(i+1)*m]
    insertion_sort(0, n/m-1,
                   lambda k: items[k*m],
                   lambda i, j: -1 if (i < j) else 1,
                   exchange_batch)
    # 3. merge all the blocks, should be N/M times
    for i in range(0, n/m):
        for j in range(0, n/m-1):
            merge(items, aux, j*m, (j+1)*m-1, (j+2)*m-1)

if __name__ == '__main__':
    items = [random.randint(1, 100) for _ in xrange(20)]
    print items
    m = 5
    merge_sort(items, m)
    print items
