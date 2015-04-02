#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return root

        root.next = None
        stack = [root]
        stack_next = []
        while stack:
            for n in stack:
                if n.left:
                    stack_next.append(n.left)
                if n.right:
                    stack_next.append(n.right)
            if not stack_next:
                break

            for i in range(len(stack_next) -1):
                stack_next[i].next = stack_next[i+1]
            stack_next[-1].next = None
            stack = stack_next
            stack_next = []
