#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

"""

class Solution:
    def __init__(self):
        self.cnt = 0

    def find_biggest_littles(self, A, al, ah, pivort):
        if pivort < A[al]:
            return al-1
        if pivort > A[ah]:
            return ah
        if al >= ah:
            return ah
        # find the last element in A[al:ah] that not bigger than pivort
        mid = (al + ah) / 2
        if A[mid] <= pivort < A[mid+1]:
            return mid
        elif A[mid] > pivort:
            return self.find_biggest_littles(A, al, mid, pivort)
        else:
            return self.find_biggest_littles(A, mid+1, ah, pivort)

    def find_in_1(self, A, al, ah, mpos, cand):
        r = A[al+mpos]
        c = A[al+mpos+1] if (len(A) > (al+mpos+1)) else cand
        return r, c

    def find_in_2(self, A, al, ah, B, bl, bh, mpos):
        alen, blen = ah-al+1, bh-bl+1
        if A[al] > B[bh]:
            if blen > mpos:
                return self.find_in_1(B, bl, bh, mpos, A[al])
            else:
                return self.find_in_1(A, al, ah, mpos-blen, 0)
        elif B[bl] > A[ah]:
            if alen > mpos:
                return self.find_in_1(A, al, ah, mpos, B[al])
            else:
                return self.find_in_1(B, bl, bh, mpos-alen, 0)

        if mpos < 100:
            R = A[al:al+mpos+2] + B[bl:bl+mpos+2]
            R.sort()
            return self.find_in_1(R, 0, len(R)-1, mpos, 0)

        amid = (ah + al) / 2
        bmid = self.find_biggest_littles(B, bl, bh, A[amid])

        this_len = amid - al + 1 + bmid - bl + 1
        if this_len == mpos:
            return A[amid], A[amid+1] if (A[amid+1] > B[bmid+1]) else B[bmid+1]
        elif this_len > mpos:
            return self.find_in_2(A, al, amid, B, bl, bmid, mpos)
        else:
            return self.find_in_2(A, amid+1, ah, B, bmid+1, bh, mpos - this_len)


    # @return a float
    def findMedianSortedArrays(self, A, B):
        al, bl = len(A), len(B)
        mid = (al + bl + 1) / 2 - 1
        if not A:
            r, n = self.find_in_1(B, 0, bl-1, (bl-1)/2, 0)
        elif not B:
            r, n = self.find_in_1(A, 0, al-1, (al-1)/2, 0)
        else:
            r, n = self.find_in_2(A, 0, al-1, B, 0, bl-1, mid)
        if (al % 2) == (bl % 2):
            return (r+n) / 2.0
        return r


if __name__ == '__main__':
    s = Solution()
    with open('data.txt') as f:
        for i in range(int(sys.argv[1]) * 3):
            f.readline()
        f.readline()
        l = f.readline().strip()
        a = map(int, l.split(',')) if l else []
        l = f.readline().strip()
        b = map(int, l.split(',')) if l else []

        f.close()
    print s.findMedianSortedArrays(a, b)
