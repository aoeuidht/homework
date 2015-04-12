# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None

        dh = RandomListNode(0)
        oh = head
        nh = dh
        mp = {}
        while oh:
            n = RandomListNode(oh.label)
            nh.next = n
            nh = n
            mp[id(oh)] = n

            oh = oh.next

        oh = head
        nh = dh.next
        while oh:
            if oh.random:
                nh.random = mp[id(oh.random)]
            oh = oh.next
            nh = nh.next

        return dh.next
