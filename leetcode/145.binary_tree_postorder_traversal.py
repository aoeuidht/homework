# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        rst = []
        self.p_wrapper(root, rst)
        return rst

    def p_wrapper(self, root, rst):
        if not root:
            return
        if root.left:
            self.p_wrapper(root.left, rst)
        if root.right:
            self.p_wrapper(root.right, rst)
        rst.append(root.val)
