class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        # copy the brillent idea from
        # https://leetcode.com/discuss/21113/c-o-n-complex-solution-easy-to-understand
        # and i change it a little from `` c1 = c1 | i'' to ``c1 ^= i''
        c1, c2, c3 = 0, 0, 0
        for i in A:
            c3 = c2 & i
            c2 = (c1 & i) | c2
            c1 ^= i
            c1 = c1 & (~ c3)
            c2 = c2 & (~ c3)
            c3 = 0
        return c1
