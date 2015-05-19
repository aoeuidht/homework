#!/usr/bin/env python

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.hit = False
        self.sons = [None] * 26

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        self.insert_wrapper(self.root, word)

    def insert_wrapper(self, root, word):
        if not word:
            root.hit = True
            return
        # insert current character
        c = word[0]
        idx = ord(c) - 97
        if not root.sons[idx]:
            root.sons[idx] = TrieNode()
        self.insert_wrapper(root.sons[idx], word[1:])


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        if not word:
            return True
        return self.s_wrapper(word, self.root)

    def s_wrapper(self, word, root):
        wl = len(word)
        if wl < 1:
            return root.hit

        c = word[0]
        idx = ord(c) - 97
        if idx >= 0:
            if root.sons[idx]:
                return self.s_wrapper(word[1:],
                                      root.sons[idx])
            else:
                return False

        for son in root.sons:
            if not son:
                continue
            r = self.s_wrapper(word[1:],
                               son)
            if r:
                return r
        return False

if __name__ == '__main__':
    t = WordDictionary()
    t.addWord('a')
    t.addWord('ab')
    print t.search('a')
    print t.search('a.')
    print t.search('ab')
    print t.search('.a')
