class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        elif n == 1:
            return True

        return (n % 4) > 0
