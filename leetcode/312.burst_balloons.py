class Solution(object):
    def maxCoins(self, nums):
        nl = len(nums)
        if nl == 0:
            return 0
        elif nl == 1:
            return nums[0]
        #
        dp = []
        nums.append(1)
        for i in range(nl):
            _dp = [0] * nl
            _dp[i] = nums[i-1] *  nums[i] * nums[i+1]
            #_dp[i] = nums[i]
            dp.append(_dp)
        # append extra line, so the last result will make no exception
        dp.append([0] * nl)

        # n means the length of data range
        for range_length in range(2, nl+1):
            for left in range(0, nl - range_length + 1):
                right = left + range_length - 1
                for pivort in range(left, right + 1):
                    dp[left][pivort] + nums[pivort] * nums[left - 1] * nums[right + 1] + dp[pivort+1][right]
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][pivort-1] + nums[pivort] * nums[left - 1] * nums[right + 1] + dp[pivort+1][right])
        return dp[0][nl - 1]


# """
if __name__ == '__main__':
    s = Solution()
    print s.maxCoins([3, 1, 5, 8])


# """
