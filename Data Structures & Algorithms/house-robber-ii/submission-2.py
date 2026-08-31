class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        cache=[-1]*len(nums)
        cache2=cache.copy()
        def dfs(i,l,c):
            if i>=len(l):
                return 0
            if c[i]!=-1:
                return c[i]
            c[i]=max(l[i]+dfs(i+2,l,c),dfs(i+1,l,c))
            return c[i]
        return max(dfs(0,nums[:-1],cache),dfs(0,nums[1:],cache2))
