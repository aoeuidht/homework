class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        for p in range(1, len(prices)):
            _p = prices[p] - prices[p-1]
            if _p > 0:
                profit += _p
        return profit
        
