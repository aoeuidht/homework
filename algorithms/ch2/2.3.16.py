#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random

import helper as hp

def quick_gen(lo, hi):
    cnt = hi - lo + 1
    if cnt < 3:
        return range(lo, hi+1)
    if cnt % 2:
        piv = (cnt + 1) / 2 + lo
    else:
        piv = cnt / 2 + lo - 1
    rst = [piv,]
    lowers = quick_gen(lo, piv-1)
    biggers = quick_gen(piv+1, hi)
    return rst + lowers + biggers

if __name__ == '__main__':
    print quick_gen(0, 9)
