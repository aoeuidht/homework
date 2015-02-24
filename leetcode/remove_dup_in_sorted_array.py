class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        prev_value = A[0]
        piv = 1
        for k in range(1, len(A)):
            if A[k] != prev_value:
                prev_value = A[k]
                if piv != k:
                    A[piv] = A[k]
                piv += 1
        #A[piv:] = []
        return piv
                
        
