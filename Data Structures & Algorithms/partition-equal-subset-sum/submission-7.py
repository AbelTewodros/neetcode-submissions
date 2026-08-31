class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2!=0:
            return False
        target=total/2
        memo={}
        def dfs(i,target):
        
            if i>=len(nums):
                return target==0
            if target<0:
                return False
            if (i,target) in memo.keys():
                return memo[(i,target)]
            memo[(i,target)]=dfs(i+1,target-nums[i]) or dfs(i+1,target)
            return memo[(i,target)]
            
        return dfs(0,target)
        