class Solution:
    
    def get_idx(self, i, j):
        return i, j, (j/3)*3 + i/3
        
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        a = [-1] * 9
        h = [a[:] for i in range(9)]
        v = [a[:] for i in range(9)]
        c = [a[:] for i in range(9)]
        mp = (h, v, c)
        for i, ln in enumerate(board):
            for j, cl in enumerate(ln):
                idxes = self.get_idx(i, j)
                c = ord(cl) - 49
                if -1 < c < 10:
                    for idx, lst in zip(idxes, mp):
                        if lst[idx][c] > -1:
                            return False
                        lst[idx][c] = 1
        return True
