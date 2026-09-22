class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0] = [1] * n
        for i in range(len(dp)):
            dp[i][0] = 1
        
        for idx in range(1,m):
            for j in range(1,n):
                dp[idx][j] = dp[idx-1][j]+ dp[idx][j-1]
       
        return dp[-1][-1]

            