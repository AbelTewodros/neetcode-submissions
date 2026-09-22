class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_len = 0
        idx = 0
        dp = [1] * len(nums)

        while idx < len(nums):
           
            for j in range(0,idx):
                
                if nums[j] < nums[idx]:
                    dp[idx] = max(dp[idx],dp[j]+1)
            idx += 1
        
        return max(dp)





        