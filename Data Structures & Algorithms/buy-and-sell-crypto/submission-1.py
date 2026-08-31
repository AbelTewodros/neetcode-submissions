class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        maxprof=0
        i,j=0,1
        while i<j and j<=len(prices)-1:
            print(prices[j],prices[i])
            current=prices[j]-prices[i]
            print(current)
            maxprof=max(maxprof,current)
            print(maxprof)
            if prices[i]>=prices[j]:
                i+=1
                j+=1 if i==j and j<len(prices)-1 else 0
            else:
                j+=1
        return maxprof


