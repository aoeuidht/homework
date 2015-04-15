#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import oj_helper

class ListNode:
    def __init__(self, key, x):
        self.val = x
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.usage = 0
        self.capacity = capacity
        self.key_map = {}
        self.head = ListNode(None, 0)
        self.tail = ListNode(None, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # @return an integer
    def get(self, key):
        if self.key_map.has_key(key):
            target = self.key_map[key]
            # remove target from list
            target.prev.next = target.next
            target.next.prev = target.prev

            h1 = self.head.next
            target.prev, target.next = self.head, h1
            self.head.next, h1.prev = target, target
            return target.val
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.key_map.has_key(key):
            target = self.key_map[key]
            target.val = value
            # move the latest element first
            if target.prev is self.head:
                return
            # remove target from list
            target.prev.next = target.next
            target.next.prev = target.prev

            # insert to the first
            h1 = self.head.next
            target.prev, target.next = self.head, h1
            self.head.next, h1.prev = target, target
        else:
            target = ListNode(key, value)
            self.key_map[key] = target
            h1 = self.head.next
            target.prev, target.next = self.head, h1
            self.head.next, h1.prev = target, target

            if self.usage < self.capacity:
                self.usage += 1
            else:
                # remove the last
                t1 = self.tail.prev
                del self.key_map[t1.key]
                t1.prev.next = self.tail
                self.tail.prev = t1.prev

if __name__ == '__main__':
    s = LRUCache(10)
    for i in range(10):
        s.set(i, i)
        print s.get(i), s.get(i*2)
        oj_helper.print_list(s.head)
    for i in range(10):
        s.set(i, i)
        print s.get(i), s.get(i*2)
        oj_helper.print_list(s.head)
    for i in range(10):
        s.set(i, 2*i)
        print s.get(i), s.get(i*2)
        oj_helper.print_list(s.head)

    s = LRUCache(2)
    s.set(2, 1)
    s.set(1, 1)
    print s.get(2)
    s.set(4, 1)
    print s.get(1)
    print s.get(2)
