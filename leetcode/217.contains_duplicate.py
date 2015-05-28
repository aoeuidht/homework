class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        l1 = len(nums)
        l2 = len(set(nums))
        return not (l1 == l2)
