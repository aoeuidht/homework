class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 1, (len(nums) - 1)
        if end < 2:
            return nums[0]

        while True:
            if start == end:
                return start
            # do count
            pivort_cnt, cnt = 0, 0
            pivort = (end + start) // 2
            for i in range(len(nums)):
                if nums[i] == pivort:
                    pivort_cnt += 1
                    continue
                elif start <= nums[i] < pivort:
                    cnt += 1
            if pivort_cnt > 1:
                return pivort
            if cnt > (pivort - start):
                end = pivort - 1
            else:
                start = pivort + 1


if __name__ == '__main__':
    import sys
    s = Solution()
    p = map(int, sys.argv[1].split(','))
    print p, s.findDuplicate(p)
