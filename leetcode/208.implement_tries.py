#!/usr/bin/env python

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
    # Returns if the word is in the trie.
    def search(self, word):
        r = None
        n = self.root
        for c in word:
            r = n
            idx = ord(c) - 97
            n = r.sons[idx]
            if not n:
                return False
        return n.hit

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        # travel to last
        rst = []
        r = self.root
        for c in prefix:
            if not r:
                return False
            idx = ord(c) - 97
            r = r.sons[idx]
        if not r:
            return False
        if r.hit:
            return True
            rst.append(prefix)
        stack = [(prefix, r)]
        while stack:
            prefix, n = stack.pop()

            c_idx = 96
            for s in n.sons:
                c_idx += 1
                if not s:
                    continue
                c = chr(c_idx)
                p = '%s%s' % (prefix, c)
                stack.append((p, s))
                if s.hit:
                    return True
                    rst.append(p)
        return False


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

if __name__ == '__main__':
    t = Trie()
    t.insert('somestring')
    print t.search('key')
    print t.search('somestrin')
    print t.search('somestring')
    t.insert('som')
    print t.startsWith('some')
    print t.startsWith('somenot')
    print t.startsWith('')
    print t.search('')
