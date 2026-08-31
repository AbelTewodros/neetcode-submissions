class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # So what are the possibilities
        # well the best way is to have coins sorted.
        # Why well because if we go in ascending order
        # We can either stop once the next coin is bigger than amount
        # that means if the total amount is less than the lowest coin then
        # we can return -1 right. Well now what are the possibilities.
        # assume we have coins [1,5,10] what is the lowest amount of coins
        # for 12? Well would you say you can build up to it from 0 to 12
        # Imagine a list where each index is the amount and the value is the amount of coins
        # well for 0 we initialize at 0 and go till amount +1 
        # [0,1,2,3,4,-1,-1,-1,-1,-1,-1,-1,-1]
        # How mainy do we need for 1 amount well 1 coin right.
        # For two well we need 2 same idea till 4.
        # Now at 5 what do we want to do?
        # Well the possibility is 5 1 coins or 1 5 coin right.
        # So how do we handle it.
        # Well we will loop through the coins t amount of times.
        # Each time we want to check the curr value of coin is less or equal
        # otherwise there is no point right.
        # Then we basically want to take the coin[i]+cache[i-coin[i]]->this is basically
        # the difference between what we just added and what we need to reach amount
        # So for example. For this.
        # We start at index 1 well its smaller or equal we want to set it to
        # coin[i]+cache[i-coin[i]]=1
        # coin[i]+cache[i-coin[i]]=2
        # coin[i]+cache[i-coin[i]]=3
        # coin[i]+cache[i-coin[i]]=4
        # Right. Then what do we want to do well
        # when we get to 5 there are two possibilities well 1 coin or 5 coins
        # so we would need to take the minimum.
        # So curr should always be the minimum of curr and coin[i]+cache[i-coin[i]]
        # Sorting is O(nlogn or n) then loop is o(n*amount) space used is o(amount)
        coins.sort()
        cache=[float("inf") for i in range(amount+1)]
        cache[0]=0
        for curr_amount in range(1,len(cache)):
            for curr_coin in coins:
                if curr_coin<=curr_amount:
                    cache[curr_amount]=min(cache[curr_amount],1+cache[curr_amount-curr_coin])
        if cache[-1]==float("inf"):
            return -1
        return cache[-1]