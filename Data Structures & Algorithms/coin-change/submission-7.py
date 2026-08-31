class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo=[float("inf")]*(amount+1)
        memo[0]=0
        for total in range(len(memo)):

            for coin in coins:
                if coin>total:
                    continue
                
                memo[total]=min(1+memo[total-coin],memo[total])
        if memo[-1]==float("inf"):
            return -1
        return memo[-1]