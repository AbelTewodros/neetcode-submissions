class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        

        def dfs(i,j,curr_area=0):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0:
                return 0
            grid[i][j]=0
            curr_area+=1+dfs(i,j-1,curr_area)+dfs(i,j+1,curr_area)+dfs(i+1,j,curr_area)+dfs(i-1,j,curr_area)
            
    
            return curr_area
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    curr=dfs(i,j)
                    max_area=max(max_area,curr)
        return max_area
            
            