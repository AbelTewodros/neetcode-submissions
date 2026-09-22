class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def helper(idx, holding):
            if idx >= len(prices):
                return 0
            if (idx,holding) in memo:
                return memo[(idx,holding)]
            
            if holding:
               memo[(idx,holding)]= max(helper(idx+1,holding), prices[idx]+helper(idx+2,False))
            else:
                memo[(idx,holding)]=max(helper(idx+1,holding), -prices[idx]+helper(idx+1,True))
            return memo[(idx,holding)]
        return helper(0,False)