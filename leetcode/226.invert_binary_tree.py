class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root:
            root.left, root.right = root.right, root.left
        else:
            return root

        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root
