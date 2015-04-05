class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s:
            return True
            
        rst = False
        lo, hi = 0, len(s) - 1
        while True:
            if lo >= hi:
                rst = True
                break
            if not s[lo].isalnum():
                lo += 1
                continue
            if not s[hi].isalnum():
                hi -= 1
                continue
            if s[lo].lower() == s[hi].lower():
                lo += 1
                hi -= 1
            else:
                break
        return rst
        
        
        
