class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ####Each step its either i+1 or i+2 right
        ###so we go lets take 1 and lets take 2.
        ###if we take 1 then we have 1, if we take 2 we have
        ###2. Now for the 1 we either take 2 or 3. well we take
        ###2 then total 3 or 4 then ends with that we keep 3
        ###then if we take 2 we either take 3 or 0 we end
        ###up taking 2 which is the best so we return
        ###That is brute force how to optimize?
        cache=[-1]*len(cost)
        def dfs(i):
            if i>=len(cost):
                return 0
            if cache[i]!=-1:
                curr=cache[i]
            else:
                curr=cost[i]+min(dfs(i+1),dfs(i+2))
                cache[i]=curr
            return cache[i]
        
        return min(dfs(0),dfs(1))

        