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

def get_red_str(tgt):
    return '\033[31m%s\033[0m' % str(tgt)

def print_br_bst(root, prefix=' '):
    value = get_red_str(root.value) if root.__class__.is_red(root) else root.value
    print prefix, value
    if root.__class__.is_red(root.left):
        split = get_red_str('|')
    else:
        split = '|'
    if root.right:
        if root.left:
            rprefix = prefix + ' %s ' % split
        else:
            rprefix = prefix + '   '
        print rprefix[:-1], '\\'
        print_br_bst(root.right, rprefix)
    elif root.left:
        print prefix, split
    if root.left:
        print_br_bst(root.left, prefix=prefix)
