#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cProfile

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.hit = False
        self.sons = {}

class Trie:

    def __init__(self):
        self.nodes = [[0, {}]]
        self.root = 0

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        # self.insert_wrapper(self.root, word)
        ridx = 0
        for c in word:
            n = self.nodes[ridx]
            if not n[1].has_key(c):
                self.nodes.append([0, {}])
                n[1][c] = len(self.nodes) -1
            ridx = n[1][c]
        self.nodes[ridx][0] = 1

class Solution:
    def __init__(self):
        """

        Arguments:
        - `self`:
        """
        self.pt = None
        self.t = None
        self.h = 0
        self.w = 0
        self.rst = set()
        self.words = None
        self.board = None


    def findWords(self, board, words):
        self.board = board
        # init the path tracker
        self.h = len(board)
        if self.h > 0:
            self.w = len(board[0])

        if not (self.w and self.h):
            return []

        if not words:
            return []

        self.rst = set()
        self.t = Trie()
        self.words = set(words)
        for w in self.words:
            self.t.insert(w)

        #print 'tries', self.t.nodes
        self.pt = [[0] * self.w for _ in range(self.h)]

        for line, row in [(line, row) for line in range(self.h)
                       for row in range(self.w)]:
            self.travel(line, row, self.t.nodes[0])
        r = list(self.rst)
        r.sort()
        return r


    def travel(self, line, row, node, prefix=''):
        c = self.board[line][row]
        _n = node[1].get(c, 0)
        if _n < 1:
            return
        node = self.t.nodes[_n]
        #print 'travel here, node: ', node, 'curr char: ', c, 'prefix: ', prefix, line, row
        prefix = '%s%s' % (prefix, c)
        if node[0]:
            self.rst.add(prefix)
        self.pt[line][row] = 1
        # up, down, left, right
        for l, r in [(line-1, row), (line+1, row),
                     (line, row-1), (line, row+1)]:
            if (0 <= l < self.h) and (0 <= r < self.w):
                if self.pt[l][r] > 0:
                    continue
                c = self.board[l][r]
                #print 'get c here: ', c, node, prefix, c
                _n = node[1].get(c, 0)
                if _n:
                    self.travel(l, r, node, prefix)
        self.pt[line][row] = 0


if __name__ == '__main__':
    board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
    s = Solution()
    words = ["oath","pea","eat","rain"]
    #print s.findWords(board, words), 'hahaha'
    board = ["baabab","abaaaa","abaaab","ababba","aabbab","aabbba","aabaab"]
    words = ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]
    #print s.findWords(board, words), 'hahaha'
    with open('data.txt') as f:
        l = f.readline()
        board = l[:-1].split(',')
        l = f.readline()
        words = l[:-1].split(',')
    #print map(len, (board, words))
    cProfile.run('s.findWords(board, words)')

    board = ['ab']
    words = ['ab']
    print s.findWords(board, words)
