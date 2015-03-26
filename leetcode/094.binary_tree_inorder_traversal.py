# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        rst = []
        self.t_wrapper(root, rst)
        return rst
        
    def t_wrapper(self, node, rst):
        if not node:
            return
        if node.left:
            self.t_wrapper(node.left, rst)
        rst.append(node.val)
        if node.right:
            self.t_wrapper(node.right, rst)
        
