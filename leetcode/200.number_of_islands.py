class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if not grid:
            return 0
        size = len(grid[0])
        dp = [0] * size
        ic = 0
        cmap = {}
        for line in grid:
            for idx, v in enumerate(line):
                v = int(v)
                tgt = 0
                if v != 0:
                    if idx == 0:
                        tgt = dp[idx] if dp[idx] else (ic+1)
                    else:
                        if dp[idx-1]:
                            tgt = dp[idx-1]
                        elif dp[idx]:
                            tgt = dp[idx]
                        else:
                            tgt = ic + 1

                        if (dp[idx] and dp[idx-1] and
                            (dp[idx] != dp[idx-1])):
                            # mark them same
                            cmap[dp[idx]].append(dp[idx-1])
                            cmap[dp[idx-1]].append(dp[idx])
                    if tgt > ic:
                        ic = tgt
                        cmap[tgt] = []
                dp[idx] = tgt
            print dp
        cset = set()
        cnt = 0
        for i in range(1, ic+1):
            if i in cset:
                continue
            cnt += 1
            cset.add(i)
            stack = [i]
            while stack:
                k = stack.pop()
                for j in cmap[k]:
                    if not j in cset:
                        stack.append(j)
                    cset.add(j)
        print ic
        return cnt

if __name__ == '__main__':
    s = Solution()
    mat = ['11110',
           '11010',
           '11000',
           '00000']
    mat = ['11000',
           '11000',
           '00100',
           '00011']
    mat = ["1111111","0000001","1111101","1000101","1010101","1011101","1111111"]
    mat = ["01001110000010000101","10100110010101011000","01000111100000111101","11000110001110010110","01011010001001000001","10010100011010010000","10001100000100100001","10001011101011110001","10010001000000000101","00010111111111000010","10101001110110011000","01001000000111100010","10001110100010101001","00001011010101111000","01100001001110011010","10111111011010010001","10001010010100100111","00100001001101110000","00100000011010100011","10001011100101011000"]

    print s.numIslands(mat)
    for m in mat:
        print m
