# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
            
        rst = 1
        stack = [root]
        stack_bak = []
        while stack:
            for n in stack:
                if ((n.left is None) and
                    (n.right is None)):
                        return rst
                if n.left:
                    stack_bak.append(n.left)
                if n.right:
                    stack_bak.append(n.right)
            stack = stack_bak[:]
            stack_bak = []
            rst += 1
        return rst
        
