# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return
        l, r = root.left, root.right
        root.left = None
        rst = self.f_wrapper(l, root)
        rst = self.f_wrapper(r, rst)
        rst.right = None
        return
        
    def f_wrapper(self, root, h):
        if not root:
            return h
            
        l, r = root.left, root.right
        root.left = None
        h.right = root
        h = h.right
        h = self.f_wrapper(l, h)
        return self.f_wrapper(r, h)
        
