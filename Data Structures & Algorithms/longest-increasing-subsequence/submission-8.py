class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo=[1]*(len(nums)+1)

        for i in range(len(nums)-1,-1,-1):

            for j in range(i,len(nums)):
                if nums[i]<nums[j]:
                    memo[i]=max(1+memo[j],memo[i])
        return max(memo)
                
