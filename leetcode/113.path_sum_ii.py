# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        rst = self.p_wrapper(root, sum)
        return [r[::-1] for r in rst]
        
    def p_wrapper(self, root, sum):
        if not root:
            return []
            
        if (root.val == sum) and (not (root.left or root.right)):
            return [[root.val]]
            
        sum -= root.val
        
        l = self.p_wrapper(root.left, sum)
        r = self.p_wrapper(root.right, sum)
        rst = l + r
        [i.append(root.val) for i in rst]
        return rst
