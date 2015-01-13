#! /usr/bin/env python
#! -*- coding: utf-8 -*-

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
        pass

    @staticmethod
    def insert_wrapper(root, node):
        root.count += 1
        if bst.comp(root, node) > 0:
            if node.left:
                bst.insert_wrapper(node.left, node)
            else:
                root.left = node
            root.height = max(root.height, root.left.height+1)
        else:
            if node.right:
                bst.insert_wrapper(node.right, node)
            else:
                root.right = node
            root.height = max(root.height, root.right.height+1)


if __name__ == '__main__':
    pass
