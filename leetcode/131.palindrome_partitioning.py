class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        sl = len(s)
        if sl == 0:
            return []
        elif sl == 1:
            return [[s]]
        rst = []
        for i in range(1, sl+1):
            r = self.p_wrapper(s, sl, 0, i)
            if r:
                rst += r
        return rst

    def __init__(self):
        self.rc = {}

    def p_wrapper(self, s, sl, offset, num):
        k = '%d_%d' % (offset, num)
        if self.rc.has_key(k):
            return self.rc[k]

        if num == 1:
            if self.p_chk(s, offset, sl-1):
                rst = [[s[offset:sl]]]
            else:
                rst = None
        elif num == (sl - offset):
            rst = [list(s[offset:sl])]
        else:
            rst = []
            for o in range(offset, sl-num+1):
                if not self.p_chk(s, offset, o):
                    continue
                rst_l = [s[offset:o+1],]
                rst_r = self.p_wrapper(s, sl, o+1, num-1)
                if rst_r:
                    for _rst_r in rst_r:
                        rst.append(rst_l + _rst_r)
        self.rc[k] = rst
        return rst

    def p_chk(self, s, lo, hi):
        while lo < hi:
            if s[lo] == s[hi]:
                lo += 1
                hi -= 1
            else:
                return False
        return True
