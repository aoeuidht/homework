#! /usr/bin/env python
# -*- coding: utf-8 -*-



class Solution(object):
    def __init__(self):
        """

        Arguments:
        - `self`:
        """
        self.linked_head = None
        self.node_index = []

    def find_index(self, num):
        """

        Arguments:
        - `self`:
        - `num`:
        """
        if not self.node_index:
            return None
        if num <= self.node_index[0][0][0]:
            return 0
        tgt_index_idx = -1
        il = len(self.node_index)
        for i in range(il-1):
            if self.node_index[i][0][0] <= num < self.node_index[i+1][0][0]:
                tgt_index_idx = i
        if tgt_index_idx < 0:
            tgt_index_idx = il - 1
        return tgt_index_idx

    def calc_smaller(self, num):
        """
        """
        tgt_index_idx = self.find_index(num)
        tgt_index = self.node_index[tgt_index_idx]
        val = 0
        for i in range(tgt_index_idx):
            val += self.node_index[i][2]
        node = tgt_index[0]
        while node:
            if node[0] < num:
                val += node[1]
                node = node[2]
            else:
                break
        self.add_num_to_linked_list(num)
        return val

    def add_num_to_linked_list(self, num):
        """

        Arguments:
        - `self`:
        - `num`:
        """
        if not self.linked_head:
            # init the linked list
            # number, number-dup-count, next
            item = [num, 1, None]
            self.linked_head = item
            # (item, current-section-node-count, current-section-value-sum)
            self.node_index.append([item, 1, 1])
            return
        else:
            # find the proper index
            il = len(self.node_index)
            tgt_index_idx = self.find_index(num)
            tgt_index = self.node_index[tgt_index_idx]
            # do real insert
            insert_after = None
            init_node = tgt_index[0]
            for i in range(tgt_index[1]):
                if init_node[0] <= num:
                    insert_after = init_node
                    init_node = init_node[2]
                else:
                    break
            if not insert_after:
                # init_node is none, insert in the 1st node
                new_node = [num, 1, tgt_index[0]]
                tgt_index[0] = new_node
                tgt_index[1] += 1
                tgt_index[2] += 1
            elif insert_after[0] == num:
                insert_after[1] += 1
                tgt_index[2] += 1
            else:
                # init_node is not none, insert after
                new_node = [num, 1, insert_after[2]]
                insert_after[2] = new_node
                tgt_index[1] += 1
                tgt_index[2] += 1
            # if current section too long, split it
            LK_CNT, LK_MAX = 100, 200
            if tgt_index[1] > LK_MAX:
                split_node = tgt_index[0]
                new_index = [split_node, 0, 0]
                for i in range(LK_CNT):
                    new_index[1] += 1
                    new_index[2] += split_node[1]
                    split_node = split_node[2]
                new_index[1] += 1
                new_index[2] += split_node[1]

                new_node_follow = [split_node[2],
                                   tgt_index[1] - new_index[1],
                                   tgt_index[2] - new_index[2]]
                split_node[2] = None
                self.node_index[tgt_index_idx] = new_index
                self.node_index.insert(tgt_index_idx + 1, new_node_follow)


    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nl = len(nums)
        if nl < 1:
            return []
        if nl < 2:
            return [0]
        rst = [0] * nl
        self.add_num_to_linked_list(nums[-1])
        for idx in range(nl - 2, -1, -1):
            num = nums[idx]
            rst[idx] = self.calc_smaller(num)
        return rst

if __name__ == '__main__':
    s = Solution()

    items = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]

    print items
    print s.countSmaller(items)
    s = Solution()
    items = [5, 2, 6, 1]
    print items
    print s.countSmaller(items)
    s = Solution()
    items = map(int, open('315.txt').readline().split(','))
    print len(items)
    print s.countSmaller(items)
