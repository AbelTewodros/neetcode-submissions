class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        c=[[-1]*2 for _ in range(len(nums))]
        def dfs(i,flag):
            if i>=len(nums) or (flag and i==len(nums)-1):
                return 0
            if c[i][flag]!=-1:
                return c[i][flag]
            c[i][flag]=max(nums[i]+dfs(i+2,flag or i==0),dfs(i+1,flag))
            return c[i][flag]
        return max(dfs(0,True),dfs(1,False))
