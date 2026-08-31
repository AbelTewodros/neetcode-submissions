class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ###Assume all our coins are sorted in ascending
        ###Then what if we build up to amount starting from 0
        ### [0,0,0,0,0,0,0] where each index is the amount we are solving for
        ### at each index in the cache we try to find the biggest we can fit
        ###Possibilities are: -there is no coin smaller or equal to amount->return -1
            # We find a coin smaller or equal o amount.
            ##If it is equal than we can set it to 1 since
            ###we know that there is no point in finding smaller since it wont be less
            #If its smaller now we have two other possibilities. 
            ##Either we take that coin/amount if there is no left over right
            ##or we take the minimum between 1+ amount of coin[amount-coin]
            ###we have to do a recursive call because the smallest might
            ###be to add that coin multiple times before going to the smallest
            ###well actually we might need to get it as many times as we can.
        coins.sort()
        cache=[float('inf') for i in range(amount+1)]
        cache[0]=0
        for i in range(len(cache)):
            for j in range(len(coins)):
                if coins[j]<=i and i-coins[j]>=0 and cache[i-coins[j]]!=float('inf'):
                    cache[i]=min(cache[i], 1+cache[i-coins[j]])
        if cache[-1]==float('inf'):
                return -1
        return cache[-1]    
            


        