class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        if num:
            r = num % 9
            return r if r else 9
        return 0
        
