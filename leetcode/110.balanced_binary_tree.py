# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        r = self.b_wrapper(root)
        return r[0]
        
    def b_wrapper(self, root):
        if not root:
            return (True, 0)
            
        l = self.b_wrapper(root.left)
        r = self.b_wrapper(root.right)
        return (True if ((l[0] is True) and
                         (r[0] is True) and
                         (abs(r[1] - l[1]) < 2)) else False,
                max(l[1], r[1]) + 1)
            
        
