#!/usr/bin/env python
# -*- coding: utf-8 -*-

# the cps version
def s(n, f):
    if n < 1:
        return f(n)
    return s(n-1,
             lambda x: f(x + n))

# the trampoline version
def t_s(n, f):
    if n < 1:
        return lambda :f(n)
    return lambda : t_s(n-1, lambda x: f(x + n))

def trampoline(f):
    while hasattr(f, '__call__'):
        f = f()
    return f

# the fibonacci
def fib_cps(n, f):
    """

    Arguments:
    - `n`: the number of fibonacci
    - `f`: the contiunation
    """
    if n < 2:
        return f(1)
    return fib_cps((n-1),
                   lambda x: fib_cps((n-2),
                                     lambda y: f(x + y)))

def fib_tramp(n, f):
    if n < 2:
        return lambda : f(1)
    return lambda : fib_tramp(n-1,
                              lambda x: lambda : fib_tramp(n-2,
                                                           lambda y: lambda: f(x + y)))



if __name__ == '__main__':
    print s(10, lambda x: x)
    print trampoline(t_s(10, lambda x: x))
    print fib_cps(10, lambda x: x)
    print trampoline(fib_tramp(10, lambda x: x))
