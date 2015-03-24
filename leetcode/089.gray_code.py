class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n < 1:
            return [0]
        rst = [0, 1]
        c = 1
        while c < n:
            b = 2 ** c
            c += 1
            rl = len(rst)
            for i in xrange(rl):
                rl -= 1
                rst.append(rst[rl] + b)
        return rst
        
        
