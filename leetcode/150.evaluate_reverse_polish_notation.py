#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        op_map = {'+': lambda x, y: x+y,
                  '-': lambda x, y: x-y,
                  '*': lambda x, y: x*y,
                  '/': lambda x, y: x / y if ((x >= 0) == (y >= 0)) else -((-x)/y)}

        operators = []
        for i in tokens:
            if op_map.has_key(i):
                op = op_map[i]
                operand = operators.pop()
                operators[-1] = op(operators[-1], operand)
            else:
                operators.append(int(i))

        return operators[-1]

if __name__ == '__main__':
    s = Solution()
    print s.evalRPN(["2", "1", "+", "3", "*"])
    print s.evalRPN(["4", "13", "5", "/", "+"])
    print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
