class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        subset=[]
        visited=[False for i in nums]
        def dfs():
            if len(subset)==len(nums):
                res.append(subset.copy())
                return
            

            for i in range(len(nums)):
                if visited[i]==False:
                    subset.append(nums[i])
                    visited[i]=True
                    dfs()
                    subset.pop()
                    visited[i]=False
        dfs()
        return res




