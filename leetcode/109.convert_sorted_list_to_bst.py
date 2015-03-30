# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        mat = []
        while head:
            mat.append(TreeNode(head.val))
            head = head.next
            
        if not mat:
            return None
        return self.s_wrapper(mat, 0, len(mat)-1)

    def s_wrapper(self, num, lo, hi):
        if lo > hi:
            return None
        elif lo == hi:
            return num[lo]

        idx = lo + self.get_root_idx(hi-lo+1, 1)
        root = num[idx]
        root.left = self.s_wrapper(num, lo, idx-1)
        root.right = self.s_wrapper(num, idx+1, hi)
        return root

    def get_root_idx(self, n, batch):
        idx = 0
        batch = 2
        hb = batch / 2
        no = n
        n -= 1
        while n > 0:
            if n > hb:
                idx += hb
            else:
                idx += n
            n -= batch
            hb = batch
            batch *= 2
        return idx        
