class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        mem=[[-1]*2 for _ in range(len(nums))]
        
    

        def dfs(i,start):
            if i>=len(nums) or (start==1 and i>=(len(nums)-1)):
                return 0
            if mem[i][start]!=-1:
                return mem[i][start]

            mem[i][start]=max(nums[i]+dfs(i+2,start or i==0),dfs(i+1,start))
            return mem[i][start]
        
        return max(dfs(0,1),dfs(1,0))
            
