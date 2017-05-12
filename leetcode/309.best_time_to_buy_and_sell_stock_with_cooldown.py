class Solution(object):
    def __init__(self):
        """

        Arguments:
        - `self`:
        """
        self.prices = None
        self.pl = 0
        self.cache = {}

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.nums = prices
        self.pl = len(prices)
        self.cache = {}
        return self.dfs(0)

    def dfs(self, start):
        """

        Arguments:
        - `self`:
        - `start`:
        """
        if start >= (self.pl - 1):
            return 0

        if start in self.cache:
            return self.cache[start]
        pstart = start
        prst = None

        pivort_end = self.pl - 1
        while start < pivort_end:
            if self.nums[start] < self.nums[start + 1]:
                break
            start += 1
        if start == pivort_end:
            self.cache[pstart] = 0
            return 0

        pivort = start + 1
        # maxium info: end, sum
        max_info = [start + 1, self.nums[pivort] - self.nums[start]]
        # 2nd-maxium info: end, sum
        max_info_2nd = []

        cur_sum = max_info[1]
        while pivort < pivort_end:
            gap = self.nums[pivort+1] - self.nums[pivort]
            if gap <= 0:
                break
            #
            cur_sum += gap
            if cur_sum > max_info[1]:
                max_info_2nd = max_info[:]
                max_info = [pivort+1, cur_sum]
            pivort += 1

        if pivort == pivort_end:
            prst = max_info[1]
            self.cache[pstart] = prst
            return prst

        # if new_sum < 0, then we no more need
        # to recalc from pivort
        new_sum = cur_sum + gap

        print pstart, start, new_sum
        if new_sum <= 0:
            if max_info_2nd:
                prst = max(max_info[1] + self.dfs(pivort + 2),
                           max_info_2nd[1] + self.dfs(pivort + 1))
                self.cache[pstart] = prst
                return prst
            else:
                prst = max(max_info[1] + self.dfs(pivort + 2),
                           self.dfs(pivort + 1))
                self.cache[pstart] = prst
                return prst
        else:
            if max_info_2nd:
                prst = max(max_info[1] + self.dfs(pivort + 2),
                           max_info_2nd[1] + self.dfs(pivort + 1),
                           new_sum + self.dfs(pivort + 1))
                self.cache[pstart] = prst
                return prst
            else:
                prst = max(max_info[1] + self.dfs(pivort + 2),
                           new_sum + self.dfs(pivort + 1))
                self.cache[pstart] = prst
                return prst
# """
s = Solution()
print s.maxProfit([1, 2, 3, 4, 0, 2])
print s.maxProfit([1, 2, 3, 9, 2, 3, 8, 10, 0, 100]), 113
print s.maxProfit([1, -2, 3]), 5
# FIXME
print s.maxProfit([6,1,3,2,4,7]), 6
print s.maxProfit([2,1,4,5,2,9,7]), 10
print s.maxProfit([2,4, 1, 7]), 6, s.cache
print s.maxProfit([5,2,3,2,6,6,2,9,1,0,7,4,5,0]), 18, s.cache
# """
