# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root:
            return False
            
        if (root.val == sum) and (not (root.left or root.right)):
            return True
            
        sum -= root.val
        
        return (self.hasPathSum(root.left, sum) or
                self.hasPathSum(root.right, sum))
        
