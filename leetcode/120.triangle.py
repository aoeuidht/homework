class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        tlen = len(triangle)
        mem = triangle[-1][:]
        for l in range(tlen-2, -1, -1):
            for i in range(0, l+1):
                mem[i] = min(mem[i], mem[i+1]) + triangle[l][i]
        return mem[0]
