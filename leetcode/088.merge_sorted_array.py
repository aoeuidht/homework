class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing(void)
    def merge(self, A, m, B, n):
        total = m + n
        while total > 0:
            total -= 1
            if m and n:
                if A[m-1] < B[n-1]:
                    n -= 1
                    A[total] = B[n]
                else:
                    m -= 1
                    A[total] = A[m]
            elif n:
                n -= 1
                A[total] = B[n]
            else:
                break
            
        
