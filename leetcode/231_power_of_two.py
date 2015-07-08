class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return (not (n & (n - 1))) if (n > 0) else False
