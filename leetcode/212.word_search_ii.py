#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cProfile

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.hit = False
        self.sons = [None] * 26

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        # self.insert_wrapper(self.root, word)
        r = self.root
        for c in word:
            idx = ord(c) - 97
            if not r.sons[idx]:
                r.sons[idx] = TrieNode()
            r = r.sons[idx]
        r.hit = True

    def insert_wrapper(self, root, word):
        if not word:
            root.hit = True
            return
        # insert current character
        r = root
        for c in word:
            idx = ord(c) - 97
            if not r.sons[idx]:
                r.sons[idx] = TrieNode()
            r = r.sons[idx]
        r.hit = True
        """
        c = word[0]
        idx = ord(c) - 97
        if not root.sons[idx]:
            root.sons[idx] = TrieNode()
        self.insert_wrapper(root.sons[idx], word[1:])
        """

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

        self.t = Trie()
        for w in set(words):
            self.t.insert(w)

        self.pt = [[0] * self.w for _ in range(self.h)]

        for line, row in [(line, row) for line in range(self.h)
                       for row in range(self.w)]:
            self.travel(line, row, self.t.root)
        r = list(self.rst)
        r.sort()
        return r


    def travel(self, line, row, node, prefix=''):
        if not node:
            return
        if node.hit:
            self.rst.add(prefix)
        self.pt[line][row] = 1
        # up, down, left, right
        for l, r in [(line-1, row), (line+1, row),
                     (line, row-1), (line, row+1)]:
            if (0 <= l < self.h) and (0 <= r < self.w):
                if self.pt[l][r] > 0:
                    continue
                c = self.board[l][r]
                _n = node.sons[ord(c) - 97]
                self.travel(l, r, _n, '%s%s' % (prefix, c))
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
    print s.findWords(board, words), 'hahaha'
    board = ["baabab","abaaaa","abaaab","ababba","aabbab","aabbba","aabaab"]
    words = ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]
    print s.findWords(board, words), 'hahaha'
    with open('data.txt') as f:
        l = f.readline()
        board = l[:-1].split(',')
        l = f.readline()
        words = l[:-1].split(',')
    print map(len, (board, words))
    cProfile.run('print s.findWords(board, words)')
