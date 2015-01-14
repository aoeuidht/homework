#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def time_calc(f, *args, **kwargv):
    """

    Arguments:
    - `f`:
    - `*args`:
    - `**kwargv`:
    """
    start_ts = time.time()
    rst = f(*args, **kwargv)
    end_ts = time.time()
    return end_ts-start_ts, rst

def print_bst(root, prefix=' '):
    print prefix, root.value
    if root.right:
        if root.left:
            rprefix = prefix + ' | '
        else:
            rprefix = prefix + '   '
        print rprefix[:-1], '\\'
        print_bst(root.right, rprefix)
    elif root.left:
        print prefix, '|'
    if root.left:
        print_bst(root.left, prefix=prefix)
