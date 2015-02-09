#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
class KMP:
    def __init__(self, pat):
        self.pat = pat
        M = len(pat)
        R = 256

        # init dfa: a 2-dimensional array
        self.dfa = [x[:] for x in [[0] * M] * R]

        self.dfa[ord(pat[0])][0] = 1
        X = 0
        for j in range(1, M):
            for c in range(R):
                self.dfa[c][j] = self.dfa[c][X]
            self.dfa[ord(pat[j])][j] = j+1
            X = self.dfa[ord(pat[j])][X]

    def search(self, txt):
        N = len(txt)
        M = len(self.pat)
        i = j = 0
        while ((i < N) and (j < M)):
            j = self.dfa[ord(txt[i])][j]
            i += 1
        if j == M:
            return i - M
        return N

class BoyerMoore:
    def __init__(self, pat):
        self.pat = pat
        M = len(pat)
        R = 256
        self.right = [-1] * 256

        for j in range(M):
            self.right[ord(pat[j])] = j

    def search(self, txt):
        N = len(txt)
        M = len(self.pat)
        skip = 0
        i = 0
        while i <= N-M:
            skip = 0
            for j in range(M-1, -1, -1):
                if pat[j] != txt[i+j]:
                    skip = j - self.right[ord(txt[i+j])]
                    skip = skip if skip > 0 else 1
                    break
            if skip == 0:
                return i
            i += skip

if __name__ == '__main__':
    pat = sys.argv[1]
    txt = sys.argv[2]

    kmp = KMP(pat)
    bm = BoyerMoore(pat)
    offset = kmp.search(txt)
    print "kmp search %s in %s" % (pat, txt)
    print txt
    print "%s %s" % (' ' * (offset-1), txt[offset: offset+len(pat)])
    offset = bm.search(txt)
    print "boyer-moore search %s in %s" % (pat, txt)
    print txt
    print "%s %s" % (' ' * (offset-1), txt[offset: offset+len(pat)])
