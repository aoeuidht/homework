# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.s_wrapper(root, 0)
        
    def s_wrapper(self, root, root_value):
        if not root:
            return 0
            
        root_v = root_value * 10 + root.val
        if not (root.left or root.right):
            return root_v
            
        lv, rv = 0, 0
        if root.left:
            lv = self.s_wrapper(root.left, root_v)
            
        if root.right:
            rv = self.s_wrapper(root.right, root_v)
            
        return lv + rv
        
        
