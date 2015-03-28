# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root:
            return self.s_wrapper(root.left, root.right)
        return True
        
    def s_wrapper(self, n0, n1):
        if id(n0) == id(n1):
            return True
        if (not n0) or (not n1):
            return False
            
        return ((n0.val == n1.val) and
                self.s_wrapper(n0.left, n1.right) and
                self.s_wrapper(n0.right, n1.left))
        
