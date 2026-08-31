class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        maxprof=0
        i,j=0,1
        while  j<=len(prices)-1:
            if prices[i]<prices[j]:
                current=prices[j]-prices[i]
                maxprof=max(maxprof,current)
            else:
                i=j
            j+=1
        return maxprof


