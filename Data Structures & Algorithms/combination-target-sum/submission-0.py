class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        curr=0
        def dfs(i):
            nonlocal res,subset,curr
            if curr==target:
                res.append(subset.copy())
                return 
            if i>=len(nums) or curr>target:
                return
            subset.append(nums[i])
            curr+=nums[i]
            dfs(i)
            subset.pop()
            curr-=nums[i]
            dfs(i+1)
            
        
        dfs(0)
        return res
            



            
            
