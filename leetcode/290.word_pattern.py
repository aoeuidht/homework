#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from oj_helper import *


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pmap = {}
        wmap = {}
        try:
            if len(pattern) <> len(str.split()):
                return False

            for (p, w) in zip(pattern,
                              str.split()):
                print p, w
                _p = wmap.get(w, '')
                _w = pmap.get(p, '')
                if _p and _w:
                    if not (_w == w):
                        return False
                    continue
                elif _p or _w:
                    return False
                wmap[w] = p
                pmap[p] = w
            return True
        except Exception as e:
            return False

if __name__ == '__main__':
    s = Solution()
    print s.wordPattern('abba', "dog cat cat dog")
    print s.wordPattern('abba', "dog cat cat fish")
    print s.wordPattern('aaaa', "dog cat cat dog")
    print s.wordPattern('abba', "dog dog dog dog")
    print s.wordPattern('aaa', "aa aa aa aa")
