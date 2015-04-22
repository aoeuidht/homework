# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.s = []
        while root:
            self.s.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.s) > 0

    # @return an integer, the next smallest number
    def next(self):
        if not self.hasNext():
            return None
        r = self.s.pop()
        # append all the right
        node = r.right
        while node:
            self.s.append(node)
            root = root.left
        return r.val



# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
