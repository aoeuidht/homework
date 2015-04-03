class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        pl = len(prices)
        pro = [0] * (pl -1)
        for i in range(pl-1):
            pro[i] = prices[i+1] - prices[i]
            
        profit = 0
        _p = 0
        for i in pro:
            _p += i
            if _p > profit:
                profit = _p
            if _p < 0:
                _p = 0
        return profit
        
