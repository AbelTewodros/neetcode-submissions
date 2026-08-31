class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2!=0:
            return False
        target=total/2

        def dfs(i,curr):
            nonlocal target
            if i>=len(nums):
                return False
            if curr==target:
                return True
            return dfs(i+1,curr+nums[i]) or dfs(i+1,curr)
            
        return dfs(0,0)
        