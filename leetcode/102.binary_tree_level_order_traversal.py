# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        rst = []
        if not root:
            return rst
        stack = [root]
        stack_new = []
        while True:
            if not stack:
                break
            rst.append([n.val for n in stack if n])
            for n in stack:
                if n.left:
                    stack_new.append(n.left)
                if n.right:
                    stack_new.append(n.right)
            stack = stack_new
            stack_new = []
        return rst
                
