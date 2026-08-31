class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        total=0
        candidates.sort()
        def dfs(i):
            nonlocal total
            if total==target:
                res.append(subset.copy())
                return
            if i==len(candidates) or total>target:
                return
            
            subset.append(candidates[i])
            total+=candidates[i]
            dfs(i+1)
            subset.pop()
            total-=candidates[i]
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return res