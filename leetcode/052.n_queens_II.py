class Solution:
    # @return an integer
    def totalNQueens(self, n):
        rst = []
        cand = range(n)
        for i in cand:
            rst = self.expand_cand(rst, cand)

        return len(rst)

    def expand_cand(self, rst, cand):
        r = []
        if not rst:
            return [[i] for i in cand]
        item_len = len(rst[0])
        for i in rst:
            for j in (set(cand) - set(i)):
                if self.chk_cand(i, j, item_len):
                    _i = i[:]
                    _i.append(j)
                    r.append(_i)
        return r
        
    def chk_cand(self, r_his, j, item_len):
        for i in range(item_len):
            if abs(i - item_len) == abs(r_his[i] - j):
                return False
        # check two queens
        return True        
