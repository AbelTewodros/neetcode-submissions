class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest=0
        prev=float("-inf")
        cache={}
        def dfs(i,prev,curr):
            nonlocal longest
            if i>=len(nums):
                longest=max(longest,curr)
                return
            if nums[i]>prev:
                dfs(i+1,nums[i],curr+1)
            dfs(i+1,prev,curr)
        dfs(0,float("-inf"),0)
        return longest

            