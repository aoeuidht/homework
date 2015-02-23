#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

"""

class Solution:
    def chk_cand(self, cand, rf, cf):
        cand.sort()
        k = '%d_%d_%d_%d' % tuple(cand)
        if not rf.has_key(k):
            rf[k] = 1
            _rf = {}
            v = True
            for p in cand:
                ck = p
                _rc = _rf.get(ck, 0)
                _rc += 1
                if _rc > cf[ck]:
                    v = False
                    break
                _rf[p] = _rc
            if v:
                return cand
        return None

    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        nl = len(num)
        if nl < 4:
            return []
        cf = {}
        cf[num[-1]] = 1
        sum_dict = {}
        for i in range(nl-1):
            k =  num[i]
            ic = cf.get(k, 0)
            ic += 1
            cf[k] = ic
            for j in range(i+1, nl):
                cand = sum_dict.get(num[i]+num[j], [])
                cand.append([num[i], num[j]])
                sum_dict[num[i]+num[j]] = cand
        # use the 2sum here get the four sum
        cands = sum_dict.keys()
        cands.sort()
        # remember the resurt calculated
        # use the sum-of-2 as the key, the offset of cands as value
        rst = []
        rf = {}
        i, j = 0, len(cands) - 1
        while True:
            l, r = cands[i], cands[j]
            if (l + r) == target:
                # return all possible resurts
                for c in [_i+_j for _i in sum_dict[l] for _j in sum_dict[r]]:
                    rst_cand = self.chk_cand(c, rf, cf)
                    if rst_cand:
                        rst.append(rst_cand)
                i += 1
                j -= 1
            elif (l + r) > target:
                j -= 1
            else:
                i += 1
            if (i > j):
                break
        rst.sort()
        return rst

if __name__ == '__main__':
    s = Solution()
    print s.fourSum(map(int,
                         sys.argv[1].split(',')), int(sys.argv[2]))
