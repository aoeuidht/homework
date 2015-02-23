#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

"""

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        nl = len(num)
        if nl < 4:
            return []
        cand = []
        cf = {}
        cf[num[-1]] = 1
        for i in range(nl-1):
            k =  num[i]
            ic = cf.get(k, 0)
            ic += 1
            cf[k] = ic
            for j in range(i+1, nl):
                #l = num[i]
                #s = num[j]
                #l, s = (l, s) if l > s else (s, l)
                #k = '%d_%d' % (l, s)
                #if not cf.has_key(k):
                #    cand.append((l+s, l))
                #    cf[k] = 1
                cand.append((num[i]+num[j], num[i]))
        # use the 2sum here get the four sum
        cands = sorted(cand, key=lambda i: i[0])

        # remember the resurt calculated
        # use the sum-of-2 as the key, the offset of cands as value
        rst = []
        rf = {}
        i, j = 0, nl * (nl - 1) / 2 - 1
        cps = None
        cps_chk = False
        while True:
            l, r = cands[i], cands[j]
            #print i, j, l[0], r[0]
            if (l[0] + r[0]) == target:
                print i, j, l[0], r[0], l[1], l[0] - l[1], r[1], r[0] - r[1]
                rst_cand = [l[1], l[0] - l[1], r[1], r[0] - r[1]]
                rst_cand.sort()
                k = '%d_%d_%d_%d' % tuple(rst_cand)
                cps = (i, j-1)
                cps_chk = False
                i += 1
                #j -= 1
                print k
                if not rf.has_key(k):
                    rf[k] = 1
                    _rf = {}
                    v = True
                    for p in rst_cand:
                        ck = p
                        _rc = _rf.get(ck, 0)
                        _rc += 1
                        if _rc > cf[ck]:
                            v = False
                            break
                        _rf[p] = _rc
                    if v:
                        rst.append(rst_cand)
            elif (l[0] + r[0]) > target:
                j -= 1
            else:
                i += 1
            if cps and cps_chk:
                i, j = cps
                cps = None
            cps_chk = True
            if (i >= j):
                break

        return rst

if __name__ == '__main__':
    s = Solution()
    print s.fourSum(map(int,
                         sys.argv[1].split(',')), int(sys.argv[2]))
