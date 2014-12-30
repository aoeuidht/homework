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
