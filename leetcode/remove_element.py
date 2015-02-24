class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if not A:
            return 0
        piv = 0
        for k in range(len(A)):
            if A[k] != elem:
                prev_value = A[k]
                if piv != k:
                    A[piv] = A[k]
                piv += 1
        return piv        
