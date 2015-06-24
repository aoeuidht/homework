#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from oj_helper import *


class literal_token(object):
    def __init__(self, value):
        self.value = value
        self.lbp = 0
    def nud(self):
        return self.value

class operator_add_token(object):
    lbp = 10
    def nud(self):
        return expression(100)
    def led(self, left):
        return left + expression(10)

class operator_sub_token(object):
    lbp = 10
    def nud(self):
        return -expression(100)
    def led(self, left):
        return left - expression(10)

class operator_mul_token(object):
    lbp = 20
    def led(self, left):
        return left * expression(20)

class operator_div_token(object):
    lbp = 20
    def led(self, left):
        return left / expression(20)

class operator_pow_token(object):
    lbp = 30
    def led(self, left):
        return left ** expression(30-1)

class end_token(object):
    lbp = -1

class left_paren_token(object):
    lbp = 100
    def led(self, left):
        return expression(9)

class right_paren_token(object):
    lbp = -101
    def led(self, left):
        expression(100)
        return left

def tokenize(program):
    nstr = []
    for i in program:
        if '0' <= i <= '9':
            nstr.append(i)
            continue
        elif nstr:
            cnum = int(''.join(nstr))
            nstr = []
            yield literal_token(cnum)
        if i == "+":
            yield operator_add_token()
        elif i == "-":
            yield operator_sub_token()
        elif i == "*":
            yield operator_mul_token()
        elif i == "/":
            yield operator_div_token()
        elif i == "(":
            yield left_paren_token()
        elif i == ')':
            yield right_paren_token()
        elif i == ' ':
            continue
        else:
            raise SyntaxError("unknown operator: %r" % operator)
    if nstr:
        yield literal_token(int(''.join(nstr)))
    yield end_token()

def expression(rbp=0):  # note that expression is a global object in this module

    global token
    t = token
    token = next()
    # left paren
    if t.lbp == 100:
        left = expression(0)
        token = next()
    else:
        left = t.nud()

    while rbp < token.lbp:
        t = token
        token = next()
        if token.lbp == 100:
            token = next()
            rst = expression(0)
            token = literal_token(rst)
        left = t.led(left)
    return left

def calculate(program):
    global token, next
    next = tokenize(program).next
    token = next()
    return expression()

class Solution:
    def calculate(self, s):
        if s:
            return calculate(s)
        return 0

if __name__ == '__main__':
    s = Solution()
    print s.calculate('1 + 1')
    print s.calculate('2-1 + 2 ')
    print s.calculate('(1+(4+5+2)-3)+(6+8)')
