#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        so = s
        s = map(ord, so)
        l = len(s)
        if l < 1:
            return ''
        elif l == 1:
            return so
        elif l == 2:
            return so if (s[0] == s[1]) else '%s%s' % (so[1], so)

        ssum = [s[0]] * l
        for i in range(1, l):
            ssum[i] = ssum[i-1] + s[i]

        tail = 0
        for x in range(l-1, 0, -1):
            # odd
            if x % 2:
                if ssum[x] == ssum[x/2] * 2:
                    m = True
                    for i in range(0, x/2+1):
                        if s[i] == s[x-i]:
                            continue
                        m = False
                        break
                    if m:
                        tail = x
                        break
            else:
                if ssum[x] - s[x/2] == ssum[x/2-1] * 2:
                    m = True
                    for i in range(0, x/2):
                        if s[i] == s[x-i]:
                            continue
                        else:
                            m = False
                            break
                    if m:
                        tail = x
                        break
        # add the missing part
        rst = list(so[tail+1:])[::-1]
        rst.append(so)
        return ''.join(rst)


if __name__ == '__main__':
    s = Solution()
    print s.shortestPalindrome('aacecaaa')
    print s.shortestPalindrome('abcd')
    print s.shortestPalindrome('abcdcba')
    print s.shortestPalindrome('abcddcba')
    print s.shortestPalindrome('aaa')
    print s.shortestPalindrome('aaaa')
    print s.shortestPalindrome('a')
    print '----------'
    print s.shortestPalindrome('aba')
    with open('data.txt') as f:
        print s.shortestPalindrome(f.read()[:-1])
