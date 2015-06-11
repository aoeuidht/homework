#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import heapq

class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        if not buildings:
            return []
        h_list = []
        rst = []
        for b in buildings:
            l, r, h = b
            #self.eat_heap(h_list, rst)
            while h_list and (h_list[0][1] <= l):
                # eat the heap
                hh, hr = heapq.heappop(h_list)
                hh = -hh
                #print 'handle ', hh, hr, rst[-1], h_list
                rb, rh = rst[-1]
                if (rb < hr):
                    # find the next h
                    __h = 0
                    while h_list:
                        _h, _r = h_list[0]
                        if hr >= _r:
                            heapq.heappop(h_list)
                        else:
                            __h = - _h
                            break
                    self.append_rst(rst, [hr, __h])

            # add to heap
            heapq.heappush(h_list, (-h, r))
            #print b, h_list, rst
            # check the result
            if (not rst) or (rst[-1][1] < h):
                self.append_rst(rst, [l, h])

        while h_list:
            # eat the heap
            hh, hr = heapq.heappop(h_list)
            hh = -hh
            rb, rh = rst[-1]
            if (rb < hr):
                # find the next h
                h = 0
                while h_list:
                    _h, _r = h_list[0]
                    if hr >= _r:
                        heapq.heappop(h_list)
                    else:
                        h = - _h
                        break
                self.append_rst(rst, [hr, h])

        return rst

    def append_rst(self, rst, v):
        if not rst:
            rst.append(v)
            return
        r, h = rst[-1]
        vr, vh = v
        if (r == vr) and (h == 0):
            rst.pop()
            self.append_rst(rst, v)
            return

        if h == vh:
            return
        rst.append(v)


if __name__ == '__main__':
    s = Solution()
    skylines = []
    with open('test.218.data') as f:
        l = f.readline()
        skylines = map(lambda item: map(int, item.split(',')),
                       l.split('],['))
        print s.getSkyline(skylines)
        print skylines[:100]


    print s.getSkyline([[2, 9, 10],
                        [3, 7, 15],
                        [5, 12, 12],
                        [15, 20, 10],
                        [19, 24, 8]])

    print s.getSkyline([[2, 9, 10]])
    print s.getSkyline([[0,2,3],[2,5,3]])
