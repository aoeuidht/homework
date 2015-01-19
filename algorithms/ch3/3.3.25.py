#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import random

import helper

class node():
    CLR_RED = 0
    CLR_BLK = 1

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.count = 1
        self.height = 1
        self.left = None
        self.right = None
        self.color = node.CLR_RED

    @staticmethod
    def get_attr(node, attr, default=0):
        return getattr(node, attr) if node else default

    @staticmethod
    def comp(n1, n2):
        if n1.key < n2.key:
            return -1
        elif n1.key == n2.key:
            return 0
        else:
            return 1

    @staticmethod
    def is_red(n):
        return node.get_attr(n, 'color', -1) == node.CLR_RED

    @staticmethod
    def is_blk(n):
        return node.get_attr(n, 'color', -1) == node.CLR_BLK


class rb_bst():
    def __init__(self):
        self.root_node = None

    @staticmethod
    def r_left(n):
        r = n.right
        n.right = r.left
        r.left = n

        r.color = n.color
        n.color = node.CLR_RED

        r.count = n.count
        n.count = 1 + node.get_attr(n.left, 'count') \
                  + node.get_attr(n.right, 'count')
        return r

    @staticmethod
    def r_right(n):
        l = n.left
        n.left = l.right
        l.right = n

        l.color = n.color
        n.color = node.CLR_RED

        l.count = n.count
        n.count = 1 + node.get_attr(n.left, 'count') \
                  + node.get_attr(n.right, 'count')

        return l

    def insert(self, n):
        """ This is the original issert
        """
        # single 2-node
        if self.root_node:
            self.root_node = rb_bst.insert_wrapper(self.root_node, n)
        else:
            self.root_node = n
        self.root_node.color = node.CLR_BLK

    @staticmethod
    def insert_wrapper(r, n):
        """ insert node n into r"""
        if not r:
            #n.color = node.CLR_BLK
            return n
        cmp = node.comp(r, n)
        if cmp > 0:
            r.left = rb_bst.insert_wrapper(r.left, n)
        elif cmp < 0:
            r.right = rb_bst.insert_wrapper(r.right, n)
        else:
            r.value = n.value

        if cmp != 0:
            r.count += 1

        # now the colors
        # left black, right red, then rotate left
        if node.is_red(r.right) and (not node.is_red(r.left)):
            r = rb_bst.r_left(r)
        # self red, left red, then rotate right
        if node.is_red(r.left) and node.is_red(r.left.left):
            r = rb_bst.r_right(r)
        # left red, right red, then filp
        if node.is_red(r.left) and node.is_red(r.right):
            rb_bst.flip_node(r)

        return r

    @staticmethod
    def flip_node(n):
        n.left.color = node.CLR_BLK
        n.right.color = node.CLR_BLK
        n.color = node.CLR_RED

    def insert234(self, n):
        pass

    def print_bst(self, root=None, prefix=' '):
        root = root if root else self.root_node
        print helper.print_bst(root, prefix)

    def print_br_bst(self, root=None, prefix=' '):
        root = root if root else self.root_node
        print helper.print_br_bst(root, prefix)

if __name__ == '__main__':
    a = range(16)
    random.shuffle(a)
    #a = ['s', 'e', 'a', 'r', 'c', 'h', 'x', 'm', 'p', 'l']
    b = rb_bst()
    print a
    for v in a:
        n = node(v, v)
        b.insert(n)
    b.print_br_bst()
