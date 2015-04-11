class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        rst = 0
        for i in A:
            rst ^= i
        return rst
