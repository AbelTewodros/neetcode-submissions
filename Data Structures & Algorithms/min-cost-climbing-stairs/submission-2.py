class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {}


        def helper(i,curr = 0):
            if i >=len(cost)-1:
                return 0
            if i in mem:
                return mem[i]

            mem[i] = min(cost[i]+helper(i+1),cost[i+1]+helper(i+2))
            return mem[i]
            

        return helper(0)