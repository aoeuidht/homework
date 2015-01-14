#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import random

import helper

class node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.count = 1
        self.height = 1
        self.left = None
        self.right = None

class bst():
    def __init__(self):
        self.root_node = None

    @staticmethod
    def comp(n1, n2):
        if n1.key < n2.key:
            return -1
        elif n1.key == n2.key:
            return 0
        else:
            return 1

    def insert(self, node):
        if self.root_node:
            bst.insert_wrapper(self.root_node, node)
        else:
            self.root_node = node

    @staticmethod
    def insert_wrapper(root, node):
        root.count += 1
        if bst.comp(root, node) > 0:
            if root.left:
                bst.insert_wrapper(root.left, node)
            else:
                root.left = node
            root.height = max(root.height, root.left.height+1)
        else:
            if root.right:
                bst.insert_wrapper(root.right, node)
            else:
                root.right = node
            root.height = max(root.height, root.right.height+1)

    def print_bst(self, root=None, prefix=' '):
        root = root if root else self.root_node
        print helper.print_bst(root, prefix)

    def est_node(self, node, nexter):
        node = node if node else self.root_node
        while node:
            next_node = nexter(node)
            if next_node:
                node = next_node
            else:
                break
        return node

    def min_node(self):
        nexter = lambda n: n.left
        return self.est_node(None, nexter)

    def max_node(self):
        nexter = lambda n: n.right
        return self.est_node(None, nexter)

    def floor(self, fk, root=None):
        root = root if root else self.root_node
        rst = root
        while root:
            if fk == root.key:
                rst = root
                break
            elif fk < root.key:
                if root.left and (rst is root):
                    rst = root.left
                root = root.left
            elif fk > root.key:
                if not (rst is root):
                    rst = root
                root = root.right
        return rst

    def ceiling(self, fk, root=None):
        root = root if root else self.root_node
        rst = root
        while root:
            if fk == root.key:
                rst = root
                break
            elif fk > root.key:
                if root.right and (rst is root):
                    rst = root.right
                root = root.right
            else:
                if not (rst is root):
                    rst = root
                root = root.left
        return rst

    def rank(self, fk, root=None):
        root = root if root else self.root_node
        while root:
            if fk == root.key:
                return (root.count - root.right.count) if root.right else root.count
            elif fk > root.key:
                root = root.right
            else:
                root = root.left
        return None


if __name__ == '__main__':
    a = range(16)
    random.shuffle(a)
    b = bst()
    print a
    for v in a:
        n = node(v, v)
        b.insert(n)
    b.print_bst()
    mnode = b.min_node()
    maxnode = b.max_node()
    print mnode.value, maxnode.value
    fl = b.floor(7)
    print fl.key
    cl = b.ceiling(7.5)
    print cl.key
    print b.rank(7)
