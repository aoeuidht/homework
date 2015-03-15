#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
"""
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        ps = path.split('/')
        trace = []
        for p in ps:
            if (not p) or (p == '.'):
                continue
            elif p == '..':
                if trace:
                    trace.pop()
            else:
                trace.append(p)

        return '/%s' % '/'.join(trace)

if __name__ == '__main__':
    s = Solution()
    print s.simplifyPath(sys.argv[1])
