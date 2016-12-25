#! /usr/bin/env python
# -*- coding: utf-8 -*-

import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if not primes:
            return 1
        ugly_list = [1]

        # in the heapq, every element is (value, current-val, offset-in-ugly-list)
        prime_q = [(prime, prime, 0) for prime in primes]
        ugly_len = 1
        while ugly_len < n:
            item = prime_q[0]
            if item[0] > ugly_list[-1]:
                ugly_list.append(item[0])
                ugly_len += 1
            update_item = (item[1] * ugly_list[item[2]+1], item[1], item[2] + 1)
            heapq.heappushpop(prime_q, update_item)
        return ugly_list[-1]


if __name__ == '__main__':
    s = Solution()
    print s.nthSuperUglyNumber(12, [2, 7, 13, 19])
    print s.nthSuperUglyNumber(30, [3,5,13,19,23,31,37,43,47,53])
    print s.nthSuperUglyNumber(100000, [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251])
