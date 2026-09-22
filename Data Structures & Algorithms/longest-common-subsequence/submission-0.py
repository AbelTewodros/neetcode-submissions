class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0]* len(text2) for _ in range(len(text1))]

        def helper(i,j):
            if i >= len(text1) or j>= len(text2):
                return 0
            if dp[i][j] != 0:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1+helper(i+1,j+1)

            else:
                dp[i][j] = max(helper(i,j+1),helper(i+1,j))
            return dp[i][j]
        
        helper(0,0)
        return dp[0][0]
        
        